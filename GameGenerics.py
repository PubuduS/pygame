import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class GameGenerics:

    def __init__(self):
        pygame.init()

    def get_screen(self, height = 250, width = 250):
        screen = pygame.display.set_mode((height, width))
        return screen

    ## Close screen
    def close_screen(self, event, active=True):

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                active = False

        if event.type == pygame.QUIT:
           active = False

        return active

    def set_display_caption_and_icon(self, caption="pygame", image="default"):
        pygame.display.set_caption(caption)

        if image != "default":
            icon = pygame.image.load(image)
            pygame.display.set_icon(icon)

