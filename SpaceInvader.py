from GameGenerics import *
from Player import Player
from Enemy import Enemy
import random

class SpaceInvader(GameGenerics):

    ## Constructor for Player class
    # Initialize the class member variables.
    # Icon made by Pixel Buddha from www.flaticon.com
    def __init__(self):

        # Initialize pygame
        super(SpaceInvader, self).__init__()

        self.set_display_caption_and_icon("Space Invaders", "images/ufo.png")
        self.x_axis_player = 370
        self.y_axis_player = 480
        self.x_axis_enemy = random.randint(0, 736)
        self.y_axis_enemy = random.randint(0, 150)
        self.screen = self.get_screen(800, 600)
        self.background = pygame.image.load("images/background.png")
        self.main_game_loop()

    ## main_game_loop will handle all the operations of the game.
    def main_game_loop(self):

        active = True
        my_player = Player()
        my_enemy = Enemy()
        changes = 0
        enemy_x_change = 0

        while active:

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                active = self.close_screen(event, active)
                changes = my_player.player_controls(event)

            self.x_axis_player += changes
            self.x_axis_player = my_player.boundary_control(self.x_axis_player)

            enemy_x_change = my_enemy.enemy_movement(self.x_axis_enemy)
            self.x_axis_enemy += enemy_x_change
            self.y_axis_enemy += my_enemy.enemy_move_down_one_row(self.y_axis_enemy)

            my_player.player(self.screen, self.x_axis_player, self.y_axis_player)
            my_enemy.enemy(self.screen, self.x_axis_enemy, self.y_axis_enemy)
            pygame.display.update()
