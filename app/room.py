
class Surface:

    def __init__(self, width, length, dirty_patches):
        self.length = length
        self.width = width
        self.dirty_patches = dirty_patches

    def in_bounds(self, x, y):
        if x>=0 and x<=self.width:
            if y>=0 and y<=self.length:
                return True
        return False

    def clean(self, x, y):
        for index, coord in enumerate(self.dirty_patches):
            if [x, y] == coord:
                del self.dirty_patches[index]
                return 1
        return 0