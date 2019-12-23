import pygame

pygame.mixer.init()

# channel = pygame.mixer.Channel(2)
sound = pygame.mixer.Sound('./media/plant/points.ogg')


# while True:
sound.play()
#     if channel.get_busy() == False:
#         channel.play(sound)