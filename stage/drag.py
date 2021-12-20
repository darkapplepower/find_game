class Drag:
        def __init__(self, size, xy, image, callback, pygame):
                self.size = size
                self.xy = xy
                self.callback = callback
                self.rect = pygame.Rect(xy, size)
                self.image = pygame.image.load(image)
                self.image = pygame.transform.scale(self.image, size)