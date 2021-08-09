import pygame
class Weathericon():
    '''天气图标'''
    def __init__(self, screen,id):
        """初始化图标并设置位置"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.id = id
        
    def pre_weather_img(self):
        #加载图形并获得外接矩形
        self.image = pygame.image.load("E:\\016-python\\pachong\\weather\\icon\\icon.zip\\天气图标\\weathercn\\"
                                       +str(self.id)+".png")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx + 90
        self.rect.centery = 150
    def blitme(self):
        self.screen.blit(self.image, self.rect)