import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.velocity = pygame.math.Vector2(0, 0)

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        white = (255, 255, 255)
        pygame.draw.circle(self.image, white, (radius, radius), radius, 2)

    
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt