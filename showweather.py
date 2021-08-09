import sys
import pygame
from weathericon import Weathericon
from location import Location
from dtime import Date
from getinfo import Info
def show_message():
    pygame.init()
    fps = 120
    FCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("天气预报")
    location = Location(screen)
    date = Date(screen)
    info = Info(screen)
    weathericon = Weathericon(screen,info.weather_code)
    bg_color = (225,200,200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        info.pre_info()
        screen.fill(bg_color)
        location.pre_loc()
        location.blitme()
        date.pre_day()
        date.pre_week_day()
        date.blitme()
        info.blitme()
        weathericon.pre_weather_img()
        weathericon.blitme()
        pygame.display.update()
        FCLOCK.tick(fps)
show_message() 