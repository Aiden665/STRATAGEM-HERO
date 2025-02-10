import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True
apple = False

randevent = pygame.USEREVENT + 1
eventrandevent = pygame.event.Event(randevent)

yellow = pygame.color.Color(180, 180, 100)
while running:
        if pygame.event.get(pygame.QUIT):
            running = False
        if pygame.event.get(randevent):
              print("EVENT")


        screen.fill((0,0,0))
        pygame.event.post(eventrandevent)


        pygame.display.flip()
        clock.tick(60)