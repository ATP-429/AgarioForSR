import pygame

class Game:
    def __init__(self, xlim, ylim):
        self.blobs = []
        self.xlim = xlim
        self.ylim = ylim

    def add_blob(self, blob):
        self.blobs.append(blob)
    
    def tick(self):
        # Update blobs
        for blob in self.blobs:
            blob.update()

    def render(self, screen, cam):
        fabric = pygame.Surface((self.xlim, self.ylim))  # Stores the rendering of the entire map. Everything is drawn on the fabric

        pygame.draw.rect(fabric, pygame.Color('white'), (0, 0, self.xlim, self.ylim))

        for blob in self.blobs:
            blob.render(fabric)
        
        cam_window = pygame.Surface((cam.get_bounds()[2], cam.get_bounds()[3]))
        cam_window.fill((0, 0, 0))
        cam_window.blit(fabric, (0, 0), (cam.get_bounds()))  # Crop the specific area seen by the camera from the fabric
        pygame.transform.scale(cam_window, screen.get_size(), screen)
