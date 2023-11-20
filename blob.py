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
        self.collision = 0  # If collision is 0 or less, it means blob can collide. This can be used as a timer to determine when a blob should become collidable after having split

        self.playerID = playerID
        self.momentum = vector.obj(x=0, y=0)
        self.timed_momentum = vector.obj(x=0, y=0)  # Used for splitting

        self.MOUSE_FORCE = 2000
        self.UNITS_PER_SQUARE = 10  # Number of units of our space present in one square unit of actual agario (Used for conveerting formulae derived from actual agario to our formulae)
        self.MOMENTUM_LOSS = 1.2

    def render(self, screen):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.get_radius())
    
    def add_momentum(self, momentum):
        self.momentum += momentum
    
    def add_timed_momentum(self, timed_momentum):
        self.timed_momentum += timed_momentum
    
    def clear_momentum(self):
        self.momentum = vector.obj(x=0, y=0)

    def get_radius(self):
        return math.sqrt(self.mass*100)

    def update(self):
        dir = vector.obj(x=self.mouseX-self.x, y=self.mouseY-self.y).unit()

        # https://www.reddit.com/r/Agario/comments/6f0njp/movement_speed_equation/
        # Formula for speed is apparently x^-0.44 * 10, where x is mass
        # We multiply by mass again, so that when the momentum is added, the mass will cancel out and the above formula will be produced
        self.add_momentum(dir*(self.mass**(-0.44)*10*self.mass*self.UNITS_PER_SQUARE))

        # Add the timed momentum
        self.add_momentum(self.timed_momentum)


        # Reduce timed momentum by some value
        self.timed_momentum /= self.MOMENTUM_LOSS

        self.x += self.momentum.x/self.mass
        self.y += self.momentum.y/self.mass

        self.clear_momentum()

        self.collision -= 1
