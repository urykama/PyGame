import controls  
import pygame
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    # важно прописать до pygame.init()
    pygame.init()
    pygame.mixer.music.load('sounds/star-wars-imperial-march.mp3')
    pygame.mixer.music.play( -1)
    s_catch = pygame.mixer.Sound('sounds/rollover-laser-blast_mknd2u4o.mp3')
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)
    while True: 
        controls.events(screen, gun, bullets, s_catch)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)

run() 
