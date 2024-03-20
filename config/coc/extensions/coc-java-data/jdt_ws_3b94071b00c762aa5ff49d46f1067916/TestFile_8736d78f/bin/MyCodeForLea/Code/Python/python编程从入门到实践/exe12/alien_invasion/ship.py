import pygame


class Ship:
    """A class that manages spacecraft"""

    def __init__(self, ai_game):
        """Initialize the spacecraft and set its initial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the spacecraft image and obtain its bounding rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # for each spacecraft,place it in the center at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimals in the attributes of the spacecraft
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据需要移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update rect accroding to self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the spacecraft an the designated location"""
        self.screen.blit(self.image, self.rect)
