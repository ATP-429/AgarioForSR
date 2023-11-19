import pygame
import math

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
        return 0.1
    
    def get_radius(self):
        return math.sqrt(self.size)

    def update(self):
        self.x += (self.mouseX-self.x)/abs(self.mouseX-self.x)*self.get_speed()