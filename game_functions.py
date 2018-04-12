#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet  
from alien import Alien
import time
time_start=0
#在bullet文件（或者说模块）中引入Bullet类
bull_num=0
key_long=False
def check_events(ai_settings, screen, ship, bullets):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship,bullets)


def update_screen(ai_settings, screen, ship,aliens,bullets):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        ship.update()
        #  在飞船和外星人后面重绘所有子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        pygame.display.flip()
        
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    global key_long
    if event.key == pygame.K_RIGHT:
            # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
    # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    #  创建一颗子弹，并将其加入到编组 bullets 中
        #fire_bullet(ai_settings, screen, ship, bullets)
        key_long=True
                
def check_keyup_events(event, ship,bullets):
    global key_long
    if event.key == pygame.K_RIGHT:
            # 向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
    # 向右移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        key_long=False
def update_bullets(bullets):
    global bull_num   #函数使用全局变量需要用global声明

    """ 更新子弹的位置，并删除已消失的子弹 """
#  更新子弹的位置
    bullets.update()
#  删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        if(bull_num!=len(bullets)):
            print(len(bullets))
        bull_num=len(bullets)
def fire_bullet(ai_settings, screen, ship, bullets):
    global key_long
    global time_start
    if((time.time()-time_start>0.1) and key_long):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        time_start=time.time()

def get_number_rows(ai_settings, ship_height, alien_height):
    """ 计算屏幕可容纳多少行外星人 """
    available_space_y = (ai_settings.screen_height -
    (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """ 计算每行可容纳多少个外星人 """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    """ 创建一个外星人并将其放在当前行 """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人群 """
    #  创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
   #  创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)



