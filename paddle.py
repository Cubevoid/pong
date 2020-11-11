"""
Paddle class for sprite
"""
import pygame

BLACK = 0, 0, 0


class Paddle(pygame.sprite.Sprite):

    screen_height: int

    def __init__(self, color: tuple, width: int, height: int, screen_height: int) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.screen_height = screen_height

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_up(self, pixels: int) -> None:
        if pixels <= self.rect.y:
            self.rect.y -= pixels
        else:
            self.rect.y = 0

    def move_down(self, pixels: int) -> None:
        if self.rect.y + self.rect.height + pixels <= self.screen_height:
            self.rect.y += pixels
        else:
            self.rect.y = self.screen_height - self.rect.height
