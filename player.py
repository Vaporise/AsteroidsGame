import pygame
from circleshape import *
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #Override the draw method
    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.polygon(screen, white, self.triangle(), 2)

def main():
    pygame.init()
    screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set display
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
   #Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))

        player.draw(screen)

        pygame.display.flip()

    pygame.quit()

main()