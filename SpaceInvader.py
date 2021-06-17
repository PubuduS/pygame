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
        self.bullet_x_axis = 0
        self.bullet_y_axis = 480
        self.screen = self.get_screen(800, 600)
        self.background = pygame.image.load("images/background.png")
        self.main_game_loop()

    ## main_game_loop will handle all the operations of the game.
    def main_game_loop(self):

        active = True
        my_player = Player()
        my_enemy = Enemy()
        changes = 0
        fire_state = "ready"

        while active:

            # Draw the background as long as our game loop is running
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                active = self.close_screen(event, active)
                control_data = my_player.player_controls(event, fire_state)
                changes = control_data[0]

                # We only need to capture these data when the fire state is ready.
                # If bullet is currently traveling we don't need these data.
                if fire_state == "ready":
                    fire_state = control_data[1]
                    self.bullet_x_axis = self.x_axis_player

            # Draw the player across screen through x axis.
            self.x_axis_player += changes
            self.x_axis_player = my_player.boundary_control(self.x_axis_player)
            my_player.player(self.screen, self.x_axis_player, self.y_axis_player)

            # Draw the enemy across x and y axis.
            enemy_x_change = my_enemy.enemy_movement(self.x_axis_enemy)
            self.x_axis_enemy += enemy_x_change
            self.y_axis_enemy += my_enemy.enemy_move_down_one_row(self.y_axis_enemy)
            my_enemy.enemy(self.screen, self.x_axis_enemy, self.y_axis_enemy)

            # When fire state is sets to fire, draw the bullet trajectory.
            if fire_state == "fire":

                self.bullet_y_axis -= 4
                my_player.fire_bullets(self.screen, self.bullet_x_axis, self.bullet_y_axis)

                # When the bullet goes outside of the border we reset it back to start.
                if self.bullet_y_axis <= -5:
                    fire_state = "ready"
                    self.bullet_y_axis = 480

            # Update everything with new changes.
            pygame.display.update()
