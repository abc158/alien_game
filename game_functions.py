#!/usr/bin/python
#coding:utf-8

import sys
import pygame
def check_events(ship):
    #""" ��Ӧ����������¼� """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            # �����ƶ��ɴ�
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
            # �����ƶ��ɴ�
                ship.moving_right = False


def update_screen(ai_settings, screen, ship):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        ship.update()
        pygame.display.flip()
        


