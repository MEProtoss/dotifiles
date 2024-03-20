LOG = '文件:{}中的方法:{}出错'.format(__file__,__name__)
def getFileRealPath(fileName):
    return os.path.join(os.path.dirname(__file__), fileName)
#4 植物类
class Plant(pygame.sprite.Sprite):
    def __init__(self):
        super(Plant, self).__init__()
        self.live=True


    def load_image(self):
        if hasattr(self, 'image') and hasattr(self, 'rect'):
            MainGame.window.blit(self.image, self.rect)
        else:
            print(LOG)
#4 存储所有植物的列表
plants_list = []
