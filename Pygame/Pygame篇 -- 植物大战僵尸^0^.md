### `Pygame`篇 -- **植物大战僵尸^0^**



#### **动画处理**

- `pygame`中无法加载`gif`图片
- 要实现动画效果
  - 每一帧加载一张图片，并`kill`之前的图片
- 下面为简单示例 

![](./res/Sun.gif)

![](./res/BucketheadZombie.gif)

- 代码如下：
  - 该实现方法也是在网上找到的
  - 将原来的`gif`处理成了`15*1`的`png`图片

这是处理后(`15帧`)的效果

![](./res/BucketheadZombie.png)

```python
# coding = utf-8

import pygame, sys
from pygame.sprite import Sprite
from pygame.sprite import Group


class Mysprite(Sprite):
    def __init__(self):
        super().__init__()
        self.mast_image = pygame.image.load('../imgs/BucketheadZombie.png')  # 读取图像
        # self.mast_image = pygame.image.load('./imgs/2223.jpg')  # 读取图像
        self.rect = self.mast_image.get_rect()  # 获取图像矩形参数
        self.frame_rect = self.rect.copy()  # 声明框架参数
        self.rect.x, self.rect.y = 1500, 300
        self.frame_rect.width /=15  # 我将图片处理成立 15 *1
        # self.frame_rect.height /= 1
        self.frame = 0
        self.last_frame = (self.rect.width // self.frame_rect.width) * (self.rect.height // self.frame_rect.height) - 1
        self.old_frame = 1
        self.last_time = 0

    def update(self):
        self.current_time = pygame.time.get_ticks()
        rate = 100  # 因为这个属性在别的地方不会有调用,所以这里我就写成了方法的局部变量
        if self.current_time >= self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 0
            self.last_time = self.current_time

        if self.old_frame != self.frame:
            self.frame_rect.x = (self.frame % 15) * self.frame_rect.width
            # self.frame_rect.y = (self.frame // 3) * self.frame_rect.height
            self.old_frame = self.frame

        self.image = self.mast_image.subsurface(self.frame_rect)  # 这里就是在生成子表面
        self.rect.x -= 1 # 移动
        print(self.rect.x)
        # print(f'{self.frame_rect}')


pygame.init()
screen = pygame.display.set_mode((1500, 600))
color = (255, 255, 255)
mysprite = Mysprite()
group = Group()
group.add(mysprite)
tick = pygame.time.Clock()

while True:
    tick.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(color)
    group.update()
    group.draw(screen)
    pygame.display.update()
```

> `run`一下

<video id="video" controls="" preload="none">
    <source id="mp4" src="./res/zombie.mp4" type="video/mp4">
</video>



#### 加载音乐

- `bgm`

```python
# 导入pygame资源包
import pygame

# 音乐的路径
file = r'./media/other/Faster.mp3'
# 初始化
pygame.mixer.init()
# 加载音乐文件
track = pygame.mixer.music.load(file)
while True:
    # 检查音乐流播放，有返回True，没有返回False
    # 如果没有音乐流则选择播放
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
```



- 音效

一般使用` pygame.mixer.Sound(文件路径)`



#### 场景切换

- 使用游戏精灵类(`pygame.sprite.Sprite`)
  - 设置`_layer`属性的值  (值越大层级越高)
  - 设置一个全局的对象组
    - `allgroup = pygame.sprite.LayeredUpdates()`
  - 要将游戏`精灵对象`加入`allgroup`
    - `allgroup.add(精灵对象)`



#### 综合效果

<video id="video" controls="" preload="none">
    <source id="mp4" src="./res/plant.mp4" type="video/mp4">
</video>



> 找了很多`gif`图片做成 **帧图**, 本来很想写下去的,植物大战僵尸这个全靠鼠标操作的游戏
>
> 在使用`pygame`对一些事件处理时，出现了冲突，后来也在网上找了好一会，也没有找到
>
> 最后这个`demo`也就废弃了几个月了，最后还是写一片博客来记录一下吧

- 目前对象的收集用的是区域判定
  - 以阳光直径为边长的正方形
  - 这种方法如果鼠标点击过快会失灵
- 事件冲突：**收集阳光的事件和选择卡片种植物有冲突**
- 有大佬知道怎么解决这个冲突的话，希望给小弟一个建议`哈O(∩_∩)O哈`！





