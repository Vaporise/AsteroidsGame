import pygame
import random
from constants import *
from circleshape import CircleShape

print("Asteroid module loaded")

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        print("Asteroid __init__ called")
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        super().wrap_position(SCREEN_WIDTH, SCREEN_HEIGHT)

print("Asteroid class defined")
print(dir(Asteroid))