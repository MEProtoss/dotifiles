# 8事件处理
def deal_events(self):
    eventList = pygame.event.get()
    for e in eventList:
        if e.type == pygame.QUIT:
            self.gameOver()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            print(e.pos)
            x = e.pos[0] // 80
            y = e.pos[1] // 80
            print(x, y)
            map = MainGame.map_list[y - 1][x]
            print(map.position)

            if e.button == 1:
                if map.can_grow and MainGame.money >= 50:
                    sunflower = Sunflower(map.position[0], map.position[1])
                    MainGame.plants_list.append(sunflower)
                    print('当前植物列表长度:{}'.format(len(MainGame.plants_list)))
                    map.can_grow = False
                    MainGame.money -= 50
            elif e.button == 3:
                if map.can_grow and MainGame.money >= 50:
                    peashooter = PeaShooter(map.position[0], map.position[1])
                    MainGame.plants_list.append(peashooter)
                    print('当前植物列表长度:{}'.format(len(MainGame.plants_list)))
                    map.can_grow = False
                    MainGame.money -= 50

                    # 8 调用事件处理的方法
                    self.deal_events()
