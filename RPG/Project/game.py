try:
    import pygame, sys
    from pygame.locals import *
    from constants import WINSURF_SIZE, BLACK
except ImportError as err:
    print("%s module failed to load!" % str(err))
    sys,exit()

class Game:
    def __init__(self):
        pygame.init()
        self.winsurf = pygame.display.set_mode(WINSURF_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Pygame RPG")

    def run(self):
        isRunning = True

        while isRunning:
            for event in pygame.event.get():
                if event.type == QUIT:
                    isRunning = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        isRunning = False

            self.draw()
            self.update()

        self.close()

    def draw(self):
        self.winsurf.fill(BLACK)

    def update(self):
        pygame.display.flip()

    def close(self):
        pygame.quit()
        sys.exit()