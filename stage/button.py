from .onclick import Click
class Button(Click):
        def __init__(self, size, xy, image, callback, pygame):
                super(Button, self).__init__(size, xy, callback, pygame)
                self.image = pygame.image.load(image)
                self.image = pygame.transform.scale(self.image, size)
        def resize(self, size, pygame):
                self.image = pygame.transform.scale(self.image, size)
                self.size = size