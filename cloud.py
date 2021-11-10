import pygame
import random

WIDTH = 1000
HEIGHT = 550
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
RED = (255, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OBLAKO")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((140, 80))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-(random.randrange(460,570)))
        self.rect.y = (HEIGHT/2)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = (WIDTH - (random.randrange(460, 570)))
            self.rect.y = (HEIGHT / 2)
            self.speedy = random.randrange(1, 4)

class Chmob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-(random.randrange(460,570)))
        self.rect.y = (HEIGHT/2)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = (WIDTH - (random.randrange(460, 570)))
            self.rect.y = (HEIGHT / 2)
            self.speedy = random.randrange(1, 4)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

player = Player()
all_sprites.add(player)
for i in range(4):
    m = Mob()
    all_sprites.add(m)
    Mob.add(m)

    c = Chmob()
    all_sprites.add(c)
    Chmob.add(c)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()