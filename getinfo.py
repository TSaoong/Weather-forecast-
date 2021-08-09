import requests
import pygame
class Info():
    """天气"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (0,0,0)
        self.font = pygame.font.Font( "C:\\Windows\\Fonts\\msyh.ttc", 30)
        self.pre_info()
    def pre_info(self): 
        url = 'https://jisutqybmf.market.alicloudapi.com/weather/query?city=%E4%B8%B0%E9%83%BD'
        Headers =  {"Authorization":"APPCODE fac5668a851b40e2af4c11149dcb9c67"}
        r = requests.get(url,headers=Headers)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        i =r.json()
        print(i)
        self.weather_code = (str(i["result"]["img"]))
        weather = str(i["result"]["weather"])
        temp = str(i["result"]["temp"])+"℃"
        self.wea_img = self.font.render(weather,True,self.color)
        self.temp_img = self.font.render(temp,True,self.color)
        self.wea_img_rect = self.wea_img.get_rect()
        self.temp_img_rect = self.temp_img.get_rect()
        self.wea_img_rect.centery = 200
        self.temp_img_rect.centery = 200
        self.wea_img_rect.x = self.screen_rect.centerx + 20
        self.temp_img_rect.x = self.screen_rect.centerx + 90
    def blitme(self):
        self.screen.blit(self.wea_img, self.wea_img_rect)
        self.screen.blit(self.temp_img, self.temp_img_rect)