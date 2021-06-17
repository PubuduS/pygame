import pygame

from GameGenerics import *


class Player(GameGenerics):

    ## Constructor for Player class
    # Initialize the class member variables.
    # space_invaders.png Icon made by Freepic from www.flaticon.com
    def __init__(self):
        super(Player, self).__init__()

        ## holds a spaceship image.
        self.player_image = "images/space_invaders.png"
        self.bullet_image = "images/bullet.png"
        self.bullet_img = pygame.image.load(self.bullet_image)
        self.player_img = pygame.image.load(self.player_image)
        self.playerX_change = 0
        self.control_data = [0, "ready"]

    ## Player funtion will draw the image across across screen.
    # param1 (screen): takes a reference to player screen.
    # param2 (x_axis): takes the x axis position which is used to draw the image.
    # param3 (y_axis): takes the y axis position which is used to draw the image.
    # return void
    def player(self, screen, x_axis=0, y_axis=0):
        screen.blit(self.player_img, (x_axis, y_axis))

    ## player_controls function allows user to calculate the left and right positions of
    # the player sprite. It returns the correct x axis coordinates according to user inputs.
    # param1 (event): takes a event.
    # return float playerX_change.
    def player_controls(self, event, fire_state):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -5
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 5

            # We only need to fire bullet when it is in ready state.
            if fire_state == "ready":
                if event.key == pygame.K_SPACE:
                    fire_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0

        self.control_data[0] = self.playerX_change
        self.control_data[1] = fire_state

        return self.control_data

    ## boundary_control function sets the boundaries across screen.
    # It will prevent player sprite from going beyond our screen.
    # param1 (x_axis): takes the position of x axis.
    # return int x_axis
    def boundary_control(self, x_axis):

        if x_axis <= 0:
            x_axis = 0
        elif x_axis >= 736:
            x_axis = 736

        return x_axis

    ## fire_bullets function draws the bullet across screen
    # param1 (screen): takes a reference to screen.
    # param2 (x_axis): takes position of x axis.
    # param3 (y_axis): takes position of y axis.
    # return void
    def fire_bullets(self, screen, x_axis, y_axis):
        screen.blit(self.bullet_img, (x_axis + 16, y_axis + 10))
