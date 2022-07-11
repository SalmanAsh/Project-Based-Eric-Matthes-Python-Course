import pygame


class BlueSky:
    """blue background"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Blue Sky')
        self.bg_colour = (0, 0, 139)

    def run_file(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.screen.fill(self.bg_colour)
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = BlueSky()
    ai.run_file()
