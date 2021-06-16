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

    ## Constructor for Player class
    # Initialize the class member variables.
    def __init__(self):
        pygame.init()

    ## get_screen function create a screen and return it.
    # param1 (height): takes the height of the screen.
    # param2 (width): takes the width of the screen.
    # return screen
    def get_screen(self, height = 250, width = 250):
        screen = pygame.display.set_mode((height, width))
        return screen

    ## close_screen function allows user to close the game screen
    # by clicking quit or pressing Esc key.
    # param1 (event): takes an event.
    # param2 (active): takes a boolean flag.
    # return active.
    def close_screen(self, event, active=True):

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                active = False

        if event.type == pygame.QUIT:
           active = False

        return active

    ## set_display_caption_and_icon function add caption and icon to game window.
    # param1 (caption): takes a string for caption.
    # param2 (image): take an icon image (Icon made by Pixel Buddha from www.flaticon.com)
    # return void
    def set_display_caption_and_icon(self, caption="pygame", image="default"):
        pygame.display.set_caption(caption)

        if image != "default":
            icon = pygame.image.load(image)
            pygame.display.set_icon(icon)

