import pygame
from random import randint, random

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    velocity: list

    def __init__(self, color, radius):
        super().__init__()

        self.image = pygame.Surface([2 * radius, 2 * radius])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.new_velocity()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def new_velocity(self):
        self.velocity = [(1 if random() < 0.5 else -1) * randint(5, 10), randint(-10, 10)]

    def update_velocity(self, multiplier):
        self.velocity = self.velocity * multiplier
