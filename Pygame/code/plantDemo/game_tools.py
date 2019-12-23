

import random
import pygame

# 设置一个屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 1400, 600)
# 设置帧率常量
FRAME_PER_SEC = 60




allgroup = pygame.sprite.LayeredUpdates()

# 僵尸1事件
CORPSE_EVENT = pygame.USEREVENT

# 阳光掉落事件
SUNSHINE_EVENT = pygame.USEREVENT + 1



GAME_START_SIGN = False

SUN_NUMS = 0

class gameSprite(pygame.sprite.Sprite):
    """ """

    def __init__(self, image_name, speed=1, x=150, y=100):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_name), (x, y))
        self.rect = self.image.get_rect()
        self.speed = speed


    def update(self):
        self.rect.x -= self.speed



class loadingBackground(gameSprite):
    """加载背景"""

    def __init__(self):
        super().__init__("./imgs/bg/Logo.jpg",speed=0,x=1400,y=600)
        self._layer = 100




class gameBackground(gameSprite):
    """游戏背景"""

    def __init__(self):
        super().__init__("./imgs/bg/background.jpg", speed=0, x=1400, y=600)
        self._layer = 10
        self.game_music = './media/other/fighting.mp3'


class barMenu(gameSprite):
    """植物槽"""
    def __init__(self):
        super().__init__("./imgs/bg/barMenu1.png",speed=0,x=800,y=100)
        self._layer = 11
        self.rect.x = 240

class sunFlowerCard(gameSprite):
    """ 阳光-卡片 """

    def __init__(self):
        super().__init__("./imgs/plant/card/SunFlower.png",speed=0,x=60,y=90)
        self._layer = 12
        self.rect.x = 244

class sunNum1(gameSprite):

    def __init__(self):
        super().__init__("./imgs/bg/sun2.png",speed=0,x=60,y=60)
        self._layer = 11
        self.rect.x = 180


class sunNum2(gameSprite):

    def __init__(self):
        super().__init__("./imgs/bg/sunNum.png", speed=0, x=60, y=40)
        self._layer = 11
        self.rect.x = 180
        self.rect.y = 60


class Corpse(gameSprite):
    """僵尸"""

    def __init__(self):
        # 1.调用父类方法创建僵尸  并添加图片
        super().__init__("./imgs/corpse_1.png")
        # 2.指定僵尸初始随机速度
        # self.speed = random.randint(1, 2)
        # 3.初始位置
        self.rect.top = 0
        self.rect.right = 1400
        max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = random.randint(0, max_y)

    def update(self):
        # 1.调用父类
        super().update()
        # 2.判断是否出屏幕，是则从精灵组删除僵尸
        if self.rect.x == 0:
            print(f"game over:坐标{self.rect}")
            # kill方法可以将精灵从精灵组中移除
            self.kill()


class Sunshine(pygame.sprite.Sprite):
    """阳光"""

    def __init__(self):
        super().__init__()
        self.mast_image = pygame.image.load('./imgs/plant/decompose/Sun.png')  # 读取图像
        self.rect = self.mast_image.get_rect()  # 获取图像矩形参数
        self.frame_rect = self.rect.copy()  # 声明框架参数
        # self.rect.bottom = 0
        self.frame_rect.width /= 22
        self.frame_rect.height /= 1
        self.frame = 0
        self.last_frame = (self.rect.width // self.frame_rect.width) * (self.rect.height // self.frame_rect.height) - 1
        self.old_frame = 1
        self.last_time = 0
        # 2.指定阳光初始随机速度
        self.speed = random.randint(1, 2)
        # 3.初始位置
        self.rect = self.mast_image.get_rect()  # 获取图像矩形参数
        max_x = SCREEN_RECT.width - 500
        self.rect.x = random.randint(0, max_x)
        self.score = 25

    def update(self,window):
        self.window = window
        self.init_sun_num()
        # 1.重写父类update
        self.current_time = pygame.time.get_ticks()
        rate = 100  # 因为这个属性在别的地方不会有调用,所以这里我就写成了方法的局部变量
        if self.current_time >= self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 0
            self.last_time = self.current_time

        if self.old_frame != self.frame:
            self.frame_rect.x = (self.frame % 22) * self.frame_rect.width
            # self.frame_rect.y = (self.frame // 1) * self.frame_rect.height
            self.old_frame = self.frame

        self.image = self.mast_image.subsurface(self.frame_rect)  # 这里就是在生成子表面
        self.rect.y += self.speed
        # 2.判断是否出屏幕，是则从精灵组删除阳光
        if self.rect.y >= SCREEN_RECT.height:
            print(f"没有采集到阳光:坐标{self.rect}")
            # kill方法可以将精灵从精灵组中移除
            self.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                # print(event.pos)
                # print('坐标：',self.rect.x,self.rect.y)
                x = self.rect.x
                y = self.rect.y
                # print('点击的坐标：',event.pos)
                if x<event.pos[0]<x+78 and y<event.pos[1]<y+78:
                    # print('收获阳光')
                    self.sun_effects()
                    self.init_sun_num(self.score)
                    self.kill()
    def sun_effects(self):
        pygame.mixer.Sound('./media/plant/points.ogg').play()

    def init_sun_num(self,num=0):

        pygame.font.init()
        font1 = pygame.font.Font(None, 30)
        global SUN_NUMS
        SUN_NUMS = int(SUN_NUMS)
        SUN_NUMS += num
        num_obj = font1.render(str(SUN_NUMS), True, (255, 255, 255))
        self.window.blit(num_obj,(190,70))



def init_music():
    # 加载背景音乐
    pygame.mixer.init()

    pygame.mixer.music.load('./media/other/Faster.mp3')
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1, 0)



