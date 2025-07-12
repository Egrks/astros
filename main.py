import pygame
from constants import *
from player import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_one = Player(x,y)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        player_one.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
        
        
        

if __name__ == "__main__":
    main()
