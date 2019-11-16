from base import Base
import pygame
import logging
import time
logger = logging.getLogger('flight')

class Flight(Base):
    def __init__(self, **kwargs):
        super(Flight, self).__init__(**kwargs)
        logger.debug('__init__')
        # Set up any instance variables
        self.brightness = 255

    def initialise_processor(self):
        self.surface = pygame.Surface((self.FLOOR_WIDTH * 2, self.FLOOR_HEIGHT * 2))
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def get_next_frame(self, weights):
        pygame.draw.rect(self.surface, (64, 64, 0),
            pygame.Rect(0, 0, self.surface.get_width(), self.surface.get_height()))

        pygame.draw.rect(self.surface, (0, 64, 255),
            pygame.Rect(0, 0, self.surface.get_width(), self.surface.get_height() / 2))
        
        pygame.event.pump()
        
        transformed = pygame.transform.rotate(self.surface, -30 * round(self.joystick.get_axis(0), 2))
        pixels = pygame.PixelArray(transformed.subsurface(pygame.Rect(
            (transformed.get_width() / 2) - self.FLOOR_WIDTH / 2,
            (transformed.get_height() / 2) - 6 - self.FLOOR_HEIGHT / 2,
            self.FLOOR_WIDTH,
            self.FLOOR_HEIGHT)))

        return [
            self.surface.unmap_rgb(pixels[x, y])
            for y in range(self.FLOOR_HEIGHT)
            for x in range(self.FLOOR_WIDTH)
        ]
