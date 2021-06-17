from GameGenerics import *


class Enemy(GameGenerics):

    ## Constructor for Player class
    # Initialize the class member variables.
    # enemy.png Icon made by smalllikeart from www.flaticon.com
    def __init__(self):
        super(Enemy, self).__init__()
        self.enemy_image = "images/enemy.png"
        self.enemy_img = pygame.image.load(self.enemy_image)
        self.flag_move_right = True
        self.flag_move_down = False

    ## enemy funtion will draw the image across across screen.
    # param1 (screen): takes a reference to player screen.
    # param2 (x_axis): takes the x axis position which is used to draw the image.
    # param3 (y_axis): takes the y axis position which is used to draw the image.
    # return void
    def enemy(self, screen, x_axis=0, y_axis=0):
        screen.blit(self.enemy_img, (x_axis, y_axis))

    ## enemy_movement function move enemies across screen
    # param1 (x_axis): takes the position of x axis.
    # return float x_axis
    def enemy_movement(self, x_axis):

        if x_axis < 0:
            self.flag_move_right = True
        elif x_axis > 736:
            self.flag_move_right = False
            self.flag_move_down = True
        elif x_axis == 0:
            self.flag_move_right = True
        elif x_axis == 736:
            self.flag_move_right = False
            self.flag_move_down = True
        elif x_axis < 736:
            self.flag_move_down = False

        if self.flag_move_right:
            x_axis = 2
        else:
            x_axis = -2

        return x_axis

    ## enemy_move_down_one_row function will move enemies one row after reaching rightmost side of our screen.
    # param1 (y_axis): takes the position of y axis.
    # return int down_by
    def enemy_move_down_one_row(self, y_axis):

        if self.flag_move_down and y_axis <= 510:
            down_by = 40
        else:
            down_by = 0

        return down_by
