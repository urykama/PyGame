import controls  
import pygame
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


class Sound():

    def init(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        # важно прописать до pygame.init()

    def run():
        pygame.init()
        pygame.mixer.music.load('sounds/star-wars-imperial-march.mp3')
        pygame.mixer.music.play(-1)
        s_catch = pygame.mixer.Sound('sounds/rollover-laser-blast_mknd2u4o.mp3')
        screen = pygame.display.set_mode((700, 700))

if __name__ == "__main__":
    Sound.run()
