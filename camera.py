class Camera:
    '''
    x, y represent center of camera 
    '''
    def __init__(self, x, y, zoom):
        self.x = x
        self.y = y
        self.zoom = zoom

        self.DEFAULT_WIDTH = 500
        self.DEFAULT_HEIGHT = 500
    
    def get_bounds(self):
        return (self.x-self.DEFAULT_WIDTH/2 * self.zoom, self.y-self.DEFAULT_HEIGHT/2 * self.zoom, self.DEFAULT_WIDTH*self.zoom, self.DEFAULT_HEIGHT*self.zoom)
    
