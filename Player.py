from GameGenerics import *


class Player(GameGenerics):

    ## Constructor for Player class
    # Initialize the class member variables.
    # space_invaders.png Icon made by Freepic from www.flaticon.com
    def __init__(self):
        super(Player, self).__init__()
        self.player_image = "images/space_invaders.png"
        self.player_img = pygame.image.load(self.player_image)
        self.playerX_change = 0

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
    def player_controls(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0

        return self.playerX_change

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
