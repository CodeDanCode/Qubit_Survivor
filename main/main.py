import pygame
import config
import screen
import player


class Main:
    def __init__(self):
        pygame.init()
        self.screen = screen.Screen()
        self.player = player.Player()


    def game(self):
        clock = pygame.time.Clock()
        while config.RUN:
            
            self.control()
            self.update()
            clock.tick(60)


    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.RUN = False
                # if event.key == pygame.K_RIGHT:
                #     self.player.walk_right()
                # if event.key == pygame.K_LEFT:
                #     self.player.walk_left()
                # if event.key == pygame.K_UP:
                #     self.player.walk_up()
                # if event.key == pygame.K_DOWN:
                #     self.player.walk_down()


    def update(self):
        # self.screen.fill(config.RED)
        # pygame.display.update()
        self.player.update()
        self.screen.update()



if __name__ == '__main__':
    game = Main()
    game.game()