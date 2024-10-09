import pygame
from circleshape import *
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED



class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self,x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
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

    def rotate(self, dt): #method to rotate player
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

def main():
    pygame.init()
    screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set display
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   #Game loop
    running = True
    while running:

        dt = clock.tick(60) / 1000 # cap frame rate at 60fps and convert ms to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))

        updateable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        

    pygame.quit()


main()