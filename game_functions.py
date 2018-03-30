#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet   
#在bullet文件（或者说模块）中引入Bullet类

def check_events(ai_settings, screen, ship, bullets):
    #""" 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship,bullets):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        ship.update()
        bullets.update()
        #  在飞船和外星人后面重绘所有子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        pygame.display.flip()
        
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
            # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
    # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    #  创建一颗子弹，并将其加入到编组 bullets 中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
            # 向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
    # 向右移动飞船
        ship.moving_left = False



