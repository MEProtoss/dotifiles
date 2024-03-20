#5 太阳类
class Sunflower(Plant):
    def __init__(self,x,y):
        super(Sunflower, self).__init__()
        self.image = pygame.image.load(getFileRealPath('imgs/sunflower.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.hp = 100

        self.time_count = 0

    #5 新增功能：生成阳光
    def produce_money(self):
        self.time_count += 1

        if self.time_count == 25:
            MainGame.money += 5
            self.time_count = 0

    def display_sunflower(self):
        MainGame.window.blit(self.image,self.rect)
