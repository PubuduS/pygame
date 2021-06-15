from GameGenerics import *


class Player(GameGenerics):
    def __init__(self, start_pos_x=370, start_pos_y=480):
        super(Player, self).__init__()
        self.playerX = start_pos_x
        self.playerY = start_pos_y
        self.playerX_change = 0

    def player(self, screen, image, x_axis=0, y_axis=0):
        player_img = pygame.image.load(image)
        screen.blit(player_img, (x_axis, y_axis))

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
