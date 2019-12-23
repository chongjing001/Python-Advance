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
