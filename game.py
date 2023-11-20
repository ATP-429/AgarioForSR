import pygame
import vector
from blob import Blob

class Game:
    def __init__(self, xlim, ylim):
        self.blobs = []
        self.xlim = xlim
        self.ylim = ylim

        self.SPLIT_MOMENTUM = 10000
        self.SPLIT_COLLISION_TIME = 25

    def add_blob(self, blob):
        self.blobs.append(blob)
    
    def split(self):
        blobs_to_split = self.blobs
        self.blobs = []

        for blob in blobs_to_split:
            blob1 = Blob(blob.x, blob.y, blob.mass/2, blob.col, blob.playerID)
            blob2 = Blob(blob.x, blob.y, blob.mass/2, blob.col, blob.playerID)
            blob2.add_timed_momentum(vector.obj(x=blob.mouseX-blob.x, y=blob.mouseY-blob.y).unit()*self.SPLIT_MOMENTUM)
            blob1.collision = self.SPLIT_COLLISION_TIME
            blob2.collision = self.SPLIT_COLLISION_TIME

            self.blobs.append(blob1)
            self.blobs.append(blob2)

    def tick(self):
        # Check blob collisions
        for blob1 in self.blobs:
            for blob2 in self.blobs:
                if blob1.collision <= 0 and blob2.collision <= 0 and blob1 != blob2 and blob1.playerID == blob2.playerID:
                    distance = vector.obj(x=blob1.x-blob2.x, y=blob1.y-blob2.y).rho
                    # If both blobs are colliding
                    if distance < blob1.get_radius()+blob2.get_radius():
                        depth = abs(blob1.get_radius()+blob2.get_radius() - distance)
                        # Normal vector pointing towards blob1's center from blob2
                        nv1 = vector.obj(x=blob1.x-blob2.x, y=blob1.y-blob2.y)/vector.obj(x=blob1.x-blob2.x, y=blob1.y-blob2.y).rho
                        nv2 = vector.obj(x=blob2.x-blob1.x, y=blob2.y-blob1.y)/vector.obj(x=blob1.x-blob2.x, y=blob1.y-blob2.y).rho  # Vice versa
                        blob1.add_momentum(nv1 * depth**1.5)
                        blob2.add_momentum(nv2 * depth**1.5)
        
        # Update blobs
        for blob in self.blobs:
            blob.update()
        

    '''Converts world coordinates to coordinates on screen'''
    def getCoordinateOnScreen(self, point, screen, cam):
        x, y = point
        relX, relY = x-cam.get_topleft()[0], y-cam.get_topleft()[1]
        ratioX, ratioY = relX/cam.get_width(), relY/cam.get_height()

        return ratioX*screen.get_width(), ratioY*screen.get_height()

    ## NOTE NOTE NOTE : ONLY WORKS IF CAMERA IS SQUARE
    '''Converts length in world units to length on screen'''
    def getLengthOnScreen(self, length, screen, cam):
        return (length/cam.get_width() * screen.get_width())

    def render(self, screen, cam):
        screen.fill((0, 0, 0))

        # Draw the white background of the map
        x1, y1 = self.getCoordinateOnScreen((0, 0), screen, cam)
        pygame.draw.rect(screen, pygame.Color('white'), (x1, y1, self.getLengthOnScreen(self.xlim, screen, cam), self.getLengthOnScreen(self.ylim, screen, cam)))

        # Draw the blobs
        for blob in self.blobs:
            x, y = self.getCoordinateOnScreen((blob.x, blob.y), screen, cam)
            pygame.draw.circle(screen, blob.col, (x, y), self.getLengthOnScreen(blob.get_radius(), screen, cam))

        # fabric = pygame.Surface((self.xlim, self.ylim))  # Stores the rendering of the entire map. Everything is drawn on the fabric

        # pygame.draw.rect(fabric, pygame.Color('white'), (0, 0, self.xlim, self.ylim))

        # for blob in self.blobs:
        #     blob.render(fabric)
        
        # cam_window = pygame.Surface((cam.get_bounds()[2], cam.get_bounds()[3]))
        # cam_window.fill((0, 0, 0))
        # cam_window.blit(fabric, (0, 0), (cam.get_bounds()))  # Crop the specific area seen by the camera from the fabric
        # pygame.transform.scale(cam_window, screen.get_size(), screen)
    
    def sync(self, blobs):
        self.blobs = blobs
