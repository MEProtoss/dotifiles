# 10 程序结束方法
def gameOver(self):
    MainGame.window.blit(self.draw_text(
        '僵尸吃掉了你的脑子', 50, (255, 0, 0)), (300, 200))

    pygame.time.wait(100)
    global GAMEOVER
    GAMEOVER = True
