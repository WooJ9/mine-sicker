import pygame as pg

pg.init()

CAPTION = "Mine-Cooker"
WIDTH = 640
HEIGHT = 360
FPS = 144

WINDOW = pg.display
WINDOW.set_caption(CAPTION)
ICON = pg.image.load('mine.png')
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode((WIDTH, HEIGHT))

RUNNING = True
RED = (255, 0, 0)
BLUE = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)

while RUNNING:
    pg.time.Clock().tick(FPS)

    SCREEN.fill(WHITE)
    pg.draw.rect(SCREEN, RED, [32, 64, 128, 128])

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            RUNNIG = False
