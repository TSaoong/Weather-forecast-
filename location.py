import pygame
class Location():
    '''地点图标'''
    def __init__(self, screen):
        """初始化图标并设置位置"""
        self.screen = screen
        #加载图形并获得外接矩形
        self.image = pygame.image.load("E:\\016-python\\pachong\\weather\\location.png")
        self.rect = self.image.get_rect()
        self.rect.center= (110,150)
        self.pre_loc()
    def pre_loc(self):
        self.color = (0,0,0)
        self.font = pygame.font.Font( "C:\\Windows\\Fonts\\msyh.ttc", 30)
        self.loc_img = self.font.render("重庆市丰都县",True,self.color)
        self.loc_img_rect = self.loc_img.get_rect()
        self.loc_img_rect.centery = 200
        self.loc_img_rect.x = 20
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.loc_img,self.loc_img_rect)