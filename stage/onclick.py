class Click:
        def __init__(self, size, xy, callback, pygame):
                self.size = size
                self.xy = xy
                self.callback = callback
                self.rect = pygame.Rect(xy, size)
        def move(self, xy):
                self.xy[0] += xy[0]
                self.xy[1] += xy[1]
                self.rect.move_ip(xy)
        @classmethod
        def checkOnClick(cls, arr, xy):
                for i in arr:
                        if isinstance(i, cls):
                                if i.rect.collidepoint(xy):
                                        i.callback()