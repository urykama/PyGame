import pygame

class Star(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Star, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 2)
        self.color = 255, 255, 255
        self.speed = 4.5
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение пришельцев"""
        self.y += 0.6
        self.rect.y = self.y
