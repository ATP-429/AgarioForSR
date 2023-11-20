class Camera:
    '''
    x, y represent center of camera 
    '''
    def __init__(self, x, y, zoom):
        self.x = x
        self.y = y
        self.zoom = zoom

        self.DEFAULT_SIZE = 2000
    
    def get_bounds(self):
        return (self.x-self.DEFAULT_SIZE/2 * self.zoom, self.y-self.DEFAULT_SIZE/2 * self.zoom, self.DEFAULT_SIZE*self.zoom, self.DEFAULT_SIZE*self.zoom)

    def get_width(self):
        return self.DEFAULT_SIZE*self.zoom
    
    def get_height(self):
        return self.DEFAULT_SIZE*self.zoom

    def get_topleft(self):
        return (self.get_bounds()[0], self.get_bounds()[1])
