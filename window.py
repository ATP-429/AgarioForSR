import pygame
from server.game import Game
from server.blob import Blob
from camera import Camera
from time import sleep

pygame.init()

screen = pygame.display.set_mode((500, 500))
 
pygame.display.set_caption('Agario')
 
running = True

game = Game(1000, 1000)
game.add_blob(Blob(50, 50, 100, pygame.Color('red')))
game.add_blob(Blob(200, 50, 1000, pygame.Color('red')))

cam = Camera(0, 0, 1)
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            cam.zoom -= event.y/10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cam.x -= 1
    if keys[pygame.K_d]:
        cam.x += 1
    if keys[pygame.K_w]:
        cam.y -= 1
    if keys[pygame.K_s]:
        cam.y += 1
    game.render(screen, cam)
    
    sleep(1/60)
    pygame.display.update()
    game.tick()

