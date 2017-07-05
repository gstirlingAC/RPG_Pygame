try:
    import pygame, sys, time
    from pygame.locals import *
    from constants import *
except ImportError as err:
    print("%s module failed to load!" % str(err))
    sys,exit()

class Game:
    def __init__(self):
        pygame.init()
        self.winsurf = pygame.display.set_mode(WINSURF_SIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Pygame RPG")

        self.fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

        self.cSec = 0
        self.cFrame = 0
        self.FPS = 0

    def run(self):
        isRunning = True

        while isRunning:
            for event in pygame.event.get():
                if event.type == QUIT:
                    isRunning = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        isRunning = False

            self.count_fps()
            self.draw()
            self.update()

        self.close()

    def draw(self):
        self.winsurf.fill(BLACK)
        self.draw_grid()
        self.show_fps()

    def update(self):
        pygame.display.flip()

    def close(self):
        pygame.quit()
        sys.exit()

    def count_fps(self):
        if self.cSec == time.strftime("%S"):
            self.cFrame += 1
        else:
            self.FPS = self.cFrame
            self.cFrame = 0
            self.cSec = time.strftime("%S")

    def show_fps(self):
        fps_overlay = self.fps_font.render("FPS: %s" % str(self.FPS), True, RED)
        self.winsurf.blit(fps_overlay, (10, 10))

    def draw_grid(self):
        for x in range(0, WINSURF_WIDTH, TILE_SIZE):
            for y in range(0, WINSURF_HEIGHT, TILE_SIZE):
                pygame.draw.rect(self.winsurf, WHITE, (x, y, TILE_SIZE + 1, TILE_SIZE + 1), 1)


