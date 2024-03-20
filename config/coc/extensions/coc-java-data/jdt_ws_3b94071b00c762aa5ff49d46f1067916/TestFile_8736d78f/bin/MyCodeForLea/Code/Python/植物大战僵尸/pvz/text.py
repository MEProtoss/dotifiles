shaoguan = 1
score = 0
remnant_score = 100
money = 200
#2 文本绘制
def draw_text(self, content, size, color):
    pygame.font.init()
    font = pygame.font.SysFont('kaiti', size)
    text = font.render(content, True, color)
    return text

#2 加载帮助提示
def load_help_text(self):
    text1 = self.draw_text('按左键种植太阳  按右键种植豌豆射手', 26, (255, 0, 0))
    MainGame.window.blit(text1, (150, 30))
