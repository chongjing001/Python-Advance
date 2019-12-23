from game_tools import *

class CorpseGame(object):

    def __init__(self):
        print("游戏初始化...")
        self.window = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.set_caption('植物大战僵尸简易版')
        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        self.creat_sprites()

        # pygame.time.set_timer(CORPSE_EVENT, 2000)
        pygame.time.set_timer(SUNSHINE_EVENT, 2000)

    def creat_sprites(self):
        self.logo = loadingBackground()

        self.bg = gameBackground()

        self.bar = barMenu()

        self.sun_card = sunFlowerCard()
        self.sun_num1 = sunNum1()
        self.sun_num2 = sunNum2()

        self.game_sprite_group = pygame.sprite.Group()

    def event_judge(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                print('坐标',event.pos[0])
                if 430 <= event.pos[0] <= 668 and 307 <= event.pos[1] <= 394:
                    global GAME_START_SIGN
                    GAME_START_SIGN = True
                    allgroup.change_layer(self.logo, -1)
                    pygame.mixer.music.load(self.bg.game_music)
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play(-1,0)

            elif event.type == CORPSE_EVENT:
                if GAME_START_SIGN:
                    corpse = Corpse()
                    self.game_sprite_group.add(corpse)

            elif event.type == SUNSHINE_EVENT:
                if GAME_START_SIGN:
                    sunshine = Sunshine()
                    self.game_sprite_group.add(sunshine)

    def __check_collide(self):
        """
        撞击事件
        :return:
        """
        pass




    def update_tools(self):

        self.game_sprite_group.update(self.window)
        self.game_sprite_group.draw(self.window)

    def add_group(self):
        allgroup.add(self.logo)
        allgroup.add(self.bg)
        allgroup.add(self.bar)
        allgroup.add(self.sun_card)
        allgroup.add(self.sun_num1)
        allgroup.add(self.sun_num2)

    def start_game(self):
        while True:
            self.add_group()
            self.clock.tick(FRAME_PER_SEC)
            self.event_judge()
            # allgroup.change_layer(self.logo,self.logo._layer)
            allgroup.update()
            allgroup.draw(self.window)
            # self.__check_collide()

            self.update_tools()


            # pygame.display.update()
            pygame.display.flip()


if __name__ == '__main__':
    init_music()
    game = CorpseGame()
    print('3')
    print('2')
    print('1')
    print('go')
    game.start_game()
