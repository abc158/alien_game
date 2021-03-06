#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #  创建一艘飞船
    ship = Ship(ai_settings,screen)
    #  创建一个外星人
    alien = Alien(ai_settings, screen)
    #  创建子弹 外星人编组
    bullets = Group()
    aliens = Group()
    #  创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.fire_bullet(ai_settings, screen, ship, bullets)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)
        
run_game()

