import pygame
import math
import vector

class Blob:
    def __init__(self, x, y, mass, col, playerID):
        self.x = x
        self.y = y
        self.mass = mass
        self.col = col
        self.mouseX = 100
        self.mouseY = 0

        self.playerID = playerID
        self.momentum = vector.obj(x=0, y=0)

        self.MOUSE_FORCE = 200

    def render(self, screen):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.get_radius())
    
    def add_momentum(self, momentum):
        self.momentum += momentum
    
    def clear_momentum(self):
        self.momentum = vector.obj(x=0, y=0)

    def get_radius(self):
        return math.sqrt(self.mass*100)

    def update(self):
        dir = vector.obj(x=self.mouseX-self.x, y=self.mouseY-self.y)
        dir = dir/dir.rho

        self.add_momentum(dir*self.MOUSE_FORCE)

        self.x += self.momentum.x/self.mass
        self.y += self.momentum.y/self.mass

        self.clear_momentum()