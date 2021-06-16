from GameGenerics import *
from Player import Player


class SpaceInvader(GameGenerics):

    ## Constructor for Player class
    # Initialize the class member variables.
    # Icon made by Pixel Buddha from www.flaticon.com
    def __init__(self):

        # Initialize pygame
        super(SpaceInvader, self).__init__()

        self.set_display_caption_and_icon("Space Invaders", "images/ufo.png")
        self.x_axis = 370
        self.y_axis = 480
        self.screen = self.get_screen(800, 600)
        self.main_game_loop()

    ## main_game_loop will handle all the operations of the game.
    # space_invaders.png Icon made by Freepic from www.flaticon.com
    def main_game_loop(self):

        active = True
        player_image = "images/space_invaders.png"
        my_player = Player()
        changes = 0

        while active:

            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                active = self.close_screen(event, active)
                changes = my_player.player_controls(event)

            self.x_axis += changes
            self.x_axis = my_player.boundary_control(self.x_axis)
            my_player.player(self.screen, player_image, self.x_axis, self.y_axis)
            pygame.display.update()
