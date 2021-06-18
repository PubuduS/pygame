from GameGenerics import *
from Player import Player
from Enemy import Enemy
import random
import math


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
        self.number_of_enemies = 6
        self.x_axis_enemy = []
        self.y_axis_enemy = []
        self.bullet_x_axis = 0
        self.bullet_y_axis = 480
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.collided_enemy_index = 0
        self.screen = self.get_screen(800, 600)
        self.background = pygame.image.load("images/background.png")
        self.enemy_starting_pos()
        self.main_game_loop()

    ## main_game_loop will handle all the operations of the game.
    def main_game_loop(self):

        active = True
        my_player = Player()
        my_enemy = Enemy()
        changes = 0
        fire_state = "ready"

        # Background Music
        mixer.music.load("sound/background.wav")
        mixer.music.play(-1)

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
            for i in range(self.number_of_enemies):
                enemy_x_change = my_enemy.enemy_movement(self.x_axis_enemy[i])
                self.x_axis_enemy[i] += enemy_x_change

                # if one enemy hit left all the enemies move down by 1 row or 40 pixel
                move_down = my_enemy.enemy_move_down_one_row(self.y_axis_enemy[i])
                if move_down == 40:
                    for j in range(self.number_of_enemies):
                        self.y_axis_enemy[j] += 40

                # Handle game over logic
                # Our spaceship y axis position is 480.
                # When enemy reaches to that position we end the game
                if self.y_axis_enemy[i] > 440:
                    for k in range(self.number_of_enemies):
                        self.y_axis_enemy[k] = 700
                        self.game_over_scree()
                    break

                # Draw the enemy
                my_enemy.enemy(self.screen, self.x_axis_enemy[i], self.y_axis_enemy[i])

            # When fire state is sets to fire, draw the bullet trajectory.
            if fire_state == "fire":

                self.bullet_y_axis -= 4
                my_player.fire_bullets(self.screen, self.bullet_x_axis, self.bullet_y_axis)

                # When the bullet goes outside of the border we reset it back to start.
                if self.bullet_y_axis <= -5:
                    fire_state = "ready"
                    self.bullet_y_axis = 480

            fire_state = self.handle_collisions(fire_state, self.is_collide())
            self.show_score()
            # Update everything with new changes.
            pygame.display.update()

    ## is_collide function checks the collusion between bullet and enemy
    # It returns True if enemy is hit by a bullet.
    # This function use distant formula to calculate the collusion.
    # distance = square( (x2 - x1)^2 + (y2-y1)^2 )
    # return boolean
    def is_collide(self):

        for i in range(self.number_of_enemies):

            bullet_x = self.bullet_x_axis
            bullet_y = self.bullet_y_axis

            x_diff_into_two = math.pow(self.x_axis_enemy[i] - bullet_x, 2)
            y_diff_into_two = math.pow(self.y_axis_enemy[i] - bullet_y, 2)

            distance = math.sqrt(x_diff_into_two + y_diff_into_two)

            if distance < 27:
                self.collided_enemy_index = i
                self.score += 5
                explosion_sound = mixer.Sound("sound/explosion.wav")
                explosion_sound.play()
                return True

        return False

    ## fire_bullets function draws the bullet across screen
    # param1 (fire_state): takes a reference to fire_state.
    # param2 (is_collide): takes is_collide flag.
    # return boolean fire_state
    def handle_collisions(self, fire_state, is_collide):

        if is_collide:
            for i in range(self.number_of_enemies):
                fire_state = "ready"
                self.bullet_y_axis = 480
                self.x_axis_enemy[self.collided_enemy_index] = random.randint(0, 735)
                self.y_axis_enemy[self.collided_enemy_index] = random.randint(0, 150)

        return fire_state

    ## show_score function displays the score
    # Everytime you killed an enemy, you will earn 5 points.
    # param1 (text_x_axis): x axis position of the score
    # param2 (text_y_axis): y axis position of the score
    # return void
    def show_score(self, text_x_axis=10, text_y_axis=10):
        score = self.font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score, (text_x_axis, text_y_axis))

    ## enemy_starting_pos function calculate the stating position of the enemy.
    # The starting position will be random for each turn.
    # return void
    def enemy_starting_pos(self):
        for i in range(self.number_of_enemies):
            self.x_axis_enemy.append(random.randint(0, 735))
            self.y_axis_enemy.append(random.randint(0, 150))

    ## game_over_scree function display the game over screen after enemies reached to our spaceship.
    # return void
    def game_over_scree(self):
        game_over_font = pygame.font.Font("freesansbold.ttf", 64)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(game_over_text, (200, 250))
