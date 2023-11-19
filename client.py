from game import Game
from blob import Blob
from camera import Camera
import socket
import threading
import pickle

# Connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))

# Create a local copy of the game, which will keep getting synced to server's copy
local_game = Game(1000, 1000)
cam = Camera(0, 0, 1)

mouseX = 0
mouseY = 0

running = True

# Window loop
def loop():
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                cam.zoom -= event.y/10

        screenMouseX, screenMouseY = pygame.mouse.get_pos()
        cam_bounds = cam.get_bounds()

        global mouseX, mouseY

        mouseX = screenMouseX/screen.get_width() * cam_bounds[2] + cam_bounds[0]
        mouseY = screenMouseY/screen.get_height() * cam_bounds[3] + cam_bounds[1]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            cam.x -= 1
        if keys[pygame.K_d]:
            cam.x += 1
        if keys[pygame.K_w]:
            cam.y -= 1
        if keys[pygame.K_s]:
            cam.y += 1
                
        local_game.render(screen, cam)

        pygame.display.update()

threading.Thread(target=loop).start()

import pygame
conn_clock = pygame.time.Clock()

while running:
    # Read blob data from server
    blob_data = s.recv(4096)
    blobs = pickle.loads(blob_data)

    # Sync local game to data sent by server
    local_game.sync(blobs)

    # Send mouse info to server
    mouse_data = pickle.dumps((mouseX, mouseY))
    s.send(mouse_data)
    
    conn_clock.tick(30)