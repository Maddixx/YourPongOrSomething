import pygame

def main():
    pong = Pong(1360, 768)
    pong.play_game()


class Paddle:
    # The human_controlled variable is a bool that dictates if the paddle should take it's input from the player or the computer.
    def __init__(self, pos, size, human_controlled):
        pass

    # Update the paddles position, taking in either user or computer input
    # paddles should not be able to
    def update(self, dt):
        pass

    # Draw the Paddle
    def draw(self):
        pass


class Ball:

    # The ball should be centered at start heading in a random direction.
    def __init__(self, pos, velocity):
        self.pos = pos
        self.velocity = velocity
        self.radius = 50

    # Handle physics of ball. Movement, collision, etc.
    def update(self, dt):
        pass

    # Draw the Ball
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,1), self.pos, self.radius)

    # Reverse the horizontal velocity of the ball
    def bounce_horizontal(self):
        pass

    # Reverse the vertical velocity of the ball
    def bounce_vertical(self):
        pass


# Keeps track of displaying the scores
class ScoreKeeper:
    player_score = 0
    computer_score = 0

    def __init__(self):
        pass

    # Draw the score board
    def draw(self):
        pass

    def award_player_point(self):
        pass

    def award_computer_point(self):
        pass

    # This should be called after the game is over to reset the score.
    def reset_score(self):
        pass


# Encapsulates the entire game into an object.
class Pong:
    is_running = False

    # Create drawing window intialize game objects
    def __init__(self, width, height):
        pygame.init()
        self.ball = Ball((int(width/2), int(height/2)),(0,0))
        self.screen = pygame.display.set_mode((width, height))

    # Resets the score and positions of objects.
    def reset_game(self):
        pass

    # Initiates a game returning who won as a string, ("player", "computer")
    def play_game(self):
        is_running = True
        while is_running:
            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    is_running = False
            self.ball.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    main()