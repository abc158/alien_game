#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet   
import time
time_start=0
#在bullet文件（或者说模块）中引入Bullet类
bull_num=0
key_long=False
def check_events(ai_settings, screen, ship, bullets):
    #""" 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship,bullets)


def update_screen(ai_settings, screen, ship,bullets):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        ship.update()
        #  在飞船和外星人后面重绘所有子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
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

#""" 更新子弹的位置，并删除已消失的子弹 """
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


