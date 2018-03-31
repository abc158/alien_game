#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet   
import time
time_start=0
#��bullet�ļ�������˵ģ�飩������Bullet��
bull_num=0
key_long=False
def check_events(ai_settings, screen, ship, bullets):
    #""" ��Ӧ����������¼� """
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
        #  �ڷɴ��������˺����ػ������ӵ�
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        pygame.display.flip()
        
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    global key_long
    if event.key == pygame.K_RIGHT:
            # �����ƶ��ɴ�
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
    # �����ƶ��ɴ�
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    #  ����һ���ӵ�����������뵽���� bullets ��
        #fire_bullet(ai_settings, screen, ship, bullets)
        key_long=True
                
def check_keyup_events(event, ship,bullets):
    global key_long
    if event.key == pygame.K_RIGHT:
            # �����ƶ��ɴ�
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
    # �����ƶ��ɴ�
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        key_long=False
def update_bullets(bullets):
    global bull_num   #����ʹ��ȫ�ֱ�����Ҫ��global����

#""" �����ӵ���λ�ã���ɾ������ʧ���ӵ� """
#  �����ӵ���λ��
    bullets.update()
#  ɾ������ʧ���ӵ�
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


