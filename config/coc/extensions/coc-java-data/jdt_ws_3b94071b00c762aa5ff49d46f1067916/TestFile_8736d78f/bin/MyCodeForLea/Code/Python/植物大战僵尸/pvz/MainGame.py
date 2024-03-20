#1 引入需要的模块
import os
import time

import pygame
import random
#1 配置图片地址
IMAGE_PATH = 'imgs/C:\Users\秦皇\Desktop\pvz'

scrrr_width=800
scrrr_height =560
GAMEOVER = False
#1主程序
class MainGame():
    def init_window(self):
        pygame.display.init()
        #1创建窗口
        MainGame.window = pygame.display.set_mode([scrrr_width,scrrr_height])  
    #1开始游戏
    def start_game(self):
        #1初始化窗口
        self.init_window()
        #1只要游戏没结束，就一直循环
        while not GAMEOVER:
           
            MainGame.window.fill((255, 255, 255))
           
            pygame.display.update()
#1启动主程序
if __name__ == '__main__':
    game = MainGame()
    game.start_game()
