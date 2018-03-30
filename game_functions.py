#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet   
#��bullet�ļ�������˵ģ�飩������Bullet��

def check_events(ai_settings, screen, ship, bullets):
    #""" ��Ӧ����������¼� """
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
        #  �ڷɴ��������˺����ػ������ӵ�
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        pygame.display.flip()
        
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
            # �����ƶ��ɴ�
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
    # �����ƶ��ɴ�
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    #  ����һ���ӵ�����������뵽���� bullets ��
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
            # �����ƶ��ɴ�
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
    # �����ƶ��ɴ�
        ship.moving_left = False



