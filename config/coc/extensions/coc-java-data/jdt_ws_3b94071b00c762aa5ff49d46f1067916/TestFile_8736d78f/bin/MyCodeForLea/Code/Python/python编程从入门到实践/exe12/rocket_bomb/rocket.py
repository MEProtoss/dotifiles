import pygame

class Rocket:
    """a class for managing the rocket"""

    def __init__(self,ai_game):
        """initialize the rocket and set its location """
        self.screen = ai_game.screen #将屏幕赋给属性screen
        self.screen_rect = ai_game.screen.get_rect() #get_rect()访问屏幕的属性rectangle并将其赋给screen_rect以将飞船放到屏幕的正确位置

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()# get the rounding rectangle of the rocket
        self.rect.midbottom = self.screen_rect.midbottom #for each new rocket,palce it at the midbottom of the screen

    def blitme(self):
        """draw the rocket at the specific position"""
        self.screen.blit(self.image,self.rect)



