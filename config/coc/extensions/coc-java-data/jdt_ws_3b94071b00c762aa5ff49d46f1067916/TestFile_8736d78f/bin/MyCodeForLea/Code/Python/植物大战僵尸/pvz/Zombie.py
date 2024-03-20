# 9 僵尸类
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Zombie, self).__init__()
        self.image = pygame.image.load(getFileRealPath('imgs/zombie.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 800
        self.damage = 2
        self.speed = 1
        self.live = True
        self.stop = False

    def move_zombie(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                # 8 调用游戏结束方法
                MainGame().gameOver()

    def hit_plant(self):
        for plant in MainGame.plants_list:
            if pygame.sprite.collide_rect(self, plant):

                self.stop = True
                self.eat_plant(plant)

    def eat_plant(self, plant):

        plant.hp -= self.damage

        if plant.hp <= 0:
            a = plant.rect.y // 80 - 1
            b = plant.rect.x // 80
            map = MainGame.map_list[a][b]
            map.can_grow = True
            plant.live = False

            self.stop = False

    def display_zombie(self):
        MainGame.window.blit(self.image, self.rect)
    # 9 新增存储所有僵尸的列表
        zombie_list = []
    count_zombie = 0
    produce_zombie = 100

    def init_zombies(self):
        for i in range(1, 7):
            dis = random.randint(1, 5) * 200
            zombie = Zombie(800 + dis, i * 80)
            MainGame.zombie_list.append(zombie)

    def load_zombies(self):
        for zombie in MainGame.zombie_list:
            if zombie.live:
                zombie.display_zombie()
                zombie.move_zombie()

                zombie.hit_plant()
            else:
                MainGame.zombie_list.remove(zombie)
        # 9 调用初始化僵尸的方法
        self.init_zombies()
        self.load_zombies()
     # 9 计数器增长，每数到100，调用初始化僵尸的方法
        MainGame.count_zombie += 1
        if MainGame.count_zombie == MainGame.produce_zombie:
            self.init_zombies()
            MainGame.count_zombie = 0

        pygame.time.wait(10)
# 1 实时更新
        pygame.display.update()
