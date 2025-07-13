import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = clock.tick(60)/1000
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    
    player_one = Player(x,y)
    asteroid_field = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        updatable.update(dt)
        for item in asteroids:
            if item.collision(player_one):
                print('Game over!')
                sys.exit()
            for shot in shots:
                if item.collision(shot):
                    item.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
        
        

if __name__ == "__main__":
    main()
