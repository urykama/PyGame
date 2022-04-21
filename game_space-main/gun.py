import pygame
# from pygame.sprite import Sprite

class Gun(pygame.sprite.Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/kor1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.centery
        self.center = float(self.rect.centerx)
        self.centery = float(650)
        self.rect.bottom = self.screen_rect.bottom

        self.y = float(self.rect.y)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5
        if self.mup and self.rect.top > 0:
            self.centery -= 1.5
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 1.5

        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def create_gun(self):
        """размещение пушки по центру внизу экрана"""
        self.center = self.screen_rect.centerx
        self.centery = float(650)