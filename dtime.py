import pygame
import datetime
class Date():
    '''时间'''
    def __init__(self, screen):
        """初始化时间属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (0,0,0)
        self.font = pygame.font.Font( "C:\\Windows\\Fonts\\msyh.ttc", 30)
        #self.pre_day()
        #self.pre_week_day()
    def pre_day(self):
        day =  str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.day_image = self.font.render(day,True,self.color)
        self.day_image_rect = self.day_image.get_rect()
        self.day_image_rect.centerx = self.screen_rect.centerx
        self.day_image_rect.top = 20
    def pre_week_day(self):
        week = (datetime.datetime.now().weekday())
        dic = {0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期日"}
        week_day= str(dic[week])
        self.week_day_image = self.font.render(week_day,True,self.color)
        self.week_day_image_rect = self.day_image.get_rect()
        self.week_day_image_rect.left = 150
        self.week_day_image_rect.top = 60
    def blitme(self):
        self.screen.blit(self.day_image, self.day_image_rect)
        self.screen.blit(self.week_day_image, self.week_day_image_rect)