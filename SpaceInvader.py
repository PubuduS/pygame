from GameGenerics import *
from Player import Player


class SpaceInvader(GameGenerics):

    def __init__(self):

        ## Initialize pygame
        super(SpaceInvader, self).__init__()

        ## Icon made by Pixel Buddha from www.flaticon.com
        self.set_display_caption_and_icon("Space Invaders", "images/ufo.png")
        self.x_axis = 370
        self.y_axis = 480
        self.screen = self.get_screen(800, 600)
        self.main_game_loop()

    def main_game_loop(self):

        active = True
        ## Icon made by Freepic from www.flaticon.com
        player_image = "images/space_invaders.png"
        my_player = Player()
        changes = 0

        while active:

            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                active = self.close_screen(event, active)
                changes = my_player.player_controls(event)

            self.x_axis += changes
            my_player.player(self.screen, player_image, self.x_axis, self.y_axis)
            pygame.display.update()
