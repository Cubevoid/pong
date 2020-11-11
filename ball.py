import math

import pygame
from random import randint, random

BLACK = (0, 0, 0)
MAX_VELOCITY = 20


class Ball(pygame.sprite.Sprite):

    velocity: list

    def __init__(self, color: tuple, radius: int) -> None:
        super().__init__()

        self.image = pygame.Surface([2 * radius, 2 * radius])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.new_velocity()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def new_velocity(self) -> None:
        self.velocity = [(1 if random() < 0.5 else -1) * randint(5, 8), randint(-7, 7)]

    def update_velocity(self, multiplier: float) -> None:
        if self.velocity[0] < 0:
            new_x_velocity = math.floor(self.velocity[0] * multiplier)
        else:
            new_x_velocity = math.ceil(self.velocity[0] * multiplier)
        if self.velocity[1] < 0:
            new_y_velocity = math.floor(self.velocity[1] * multiplier)
        else:
            new_y_velocity = math.ceil(self.velocity[1] * multiplier) + randint(-2, 2)
        if abs(new_x_velocity) >= MAX_VELOCITY or abs(new_y_velocity) >= MAX_VELOCITY:
            return
        else:
            self.velocity[0], self.velocity[1] = new_x_velocity, new_y_velocity

    def bounce(self, multiplier: float) -> None:
        self.update_velocity(multiplier)
        self.velocity[0] = -self.velocity[0]
