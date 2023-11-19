import pygame
import math
import vector

class Blob:
    def __init__(self, x, y, size, col):
        self.x = x
        self.y = y
        self.size = size
        self.col = col
        self.mouseX = 100
        self.mouseY = 0

    def render(self, screen):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.get_radius())
    
    def get_speed(self):
        return 0.4
    
    def get_radius(self):
        return math.sqrt(self.size)

    def update(self):
        dir = vector.obj(x=self.mouseX-self.x, y=self.mouseY-self.y)
        dir = dir/dir.rho
        self.x += dir.x*self.get_speed()
        self.y += dir.y*self.get_speed()