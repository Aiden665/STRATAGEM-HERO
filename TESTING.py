import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True
apple = False

font = pygame.font.Font("Fonts\Hatch.ttf")


yellow = pygame.color.Color(180, 180, 100)
while running:
    if pygame.event.get(pygame.QUIT):
            running = False

          
    screen.fill((0,0,0))
    


    pygame.display.flip()
    clock.tick(60)