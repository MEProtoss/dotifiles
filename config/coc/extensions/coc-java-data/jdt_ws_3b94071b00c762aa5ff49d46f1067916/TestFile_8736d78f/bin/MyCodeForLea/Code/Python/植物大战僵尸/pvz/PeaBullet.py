# 7 豌豆子弹类
class PeaBullet(pygame.sprite.Sprite):
    def __init__(self, peashooter):
        self.live = True
        self.image = pygame.image.load(getFileRealPath('imgs/peabullet.png'))
        self.damage = 50
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.x = peashooter.rect.x + 60
        self.rect.y = peashooter.rect.y + 15

    def move_bullet(self):

        if self.rect.x < scrrr_width:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_zombie(self):
        for zombie in MainGame.zombie_list:
            if pygame.sprite.collide_rect(self, zombie):

                self.live = False

                zombie.hp -= self.damage
                if zombie.hp <= 0:
                    zombie.live = False
                    self.nextLevel()
        # 7闯关方法

    def nextLevel(self):
        MainGame.score += 20
        MainGame.remnant_score -= 20
        for i in range(1, 100):
            if MainGame.score == 100*i and MainGame.remnant_score == 0:
                MainGame.remnant_score = 100*i
                MainGame.shaoguan += 1
                MainGame.produce_zombie += 50

    def display_peabullet(self):
        MainGame.window.blit(self.image, self.rect)
        peabullet_list = []

        # 7 加载所有子弹的方法
    def load_peabullets(self):
        for b in MainGame.peabullet_list:
            if b.live:
                b.display_peabullet()
                b.move_bullet()

                b.hit_zombie()
            else:
                MainGame.peabullet_list.remove(b)
        # 7  调用加载所有子弹的方法
    self.load_peabullets()
