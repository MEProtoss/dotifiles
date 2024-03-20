import pygame 
import sys
from settings import Settings

class Rocket:
    """class for managing game resources and behaviors"""

    def __init__(self):
        """initialize the game and create the game resources"""
        pygame.init()#initialize the background
        self.settings = Settings()# Create settings instance to access settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #diplay the game window
        pygame.display.set_caption("rocket bomb!")

    def run_game(self):
        """beign the main loop of the game"""
        while True:
            # monitor keyboards and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw the screen in each loop
            self.screen.fill(self.settings.bg_color)

            # make the screen drawed recently visible
            pygame.display.flip()


if __name__ == '__main__':
    #make instance and run the game 
    ai = Rocket()
    ai.run_game()


