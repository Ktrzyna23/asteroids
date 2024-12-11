# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable,)
    pygame.init()
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatables in updatable:
            updatables.update(dt)
            screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        for asteroid in asteroid_group:
            if player.check_collision(asteroid) == True:
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick()/1000
if __name__ == "__main__":
    main()