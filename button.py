import pygame
from sys import exit
pygame.init()


main_surf = pygame.display.set_mode((800, 400))
box_surf = pygame.Surface((50, 50))
box_rect = box_surf.get_rect(center=(400, 200))
box_surf.fill('White')

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()

    main_surf.blit(box_surf, box_rect)
    pygame.display.update()
    clock.tick(60)
