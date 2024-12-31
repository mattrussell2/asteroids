import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()

    updateable = pygame.sprite.Group()
    drawables  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots      = pygame.sprite.Group()

    Player.containers = updateable, drawables
    Asteroid.containers = asteroids, updateable, drawables
    AsteroidField.containers = updateable
    Shot.containers = shots, updateable, drawables

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()

        for obj in drawables:
            obj.draw(screen)

        dt = clock.tick(60) / 1000
        pygame.display.flip()
        

if __name__ == '__main__':
    main()