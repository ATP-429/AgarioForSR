from game import Game
from blob import Blob
import pickle
import socket
import pygame
import threading

HOST = '127.0.0.1'
PORT = 5000

clock = pygame.time.Clock()

# Game code
game = Game(1000, 1000)
game.add_blob(Blob(50, 50, 100, pygame.Color('red')))
game.add_blob(Blob(200, 50, 1000, pygame.Color('red')))

def game_loop():
    while True:
        game.tick()
        clock.tick(60)

threading.Thread(target=game_loop).start()


# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Listening...")
conn, addr = s.accept()
conn_clock = pygame.time.Clock()
with conn:
    print(f"Connected by {addr}")

    while True:
        # Send blob data to client
        blob_data = pickle.dumps(game.blobs)
        conn.send(blob_data)
        conn_clock.tick(60)

        # Get mouse data from client
        mouse_data = conn.recv(4096)
        mouseX, mouseY = pickle.loads(mouse_data)

        for blob in game.blobs:
            blob.mouseX = mouseX
            blob.mouseY = mouseY