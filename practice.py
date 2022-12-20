import pygame as pg

pg.init()

CAPTION = "Mine-Cooker"
WIDTH = 640
HEIGHT = 360
FPS = 144
FONT = pg.font.SysFont("arial", 32, True, True)

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

text = FONT.render("Hello, World!", True, WHITE)
image = pg.image.load('sweeper.jpg')

while RUNNING:
    pg.time.Clock().tick(FPS)

    SCREEN.fill(BLACK)
    SCREEN.blit(text,[32, 32])
    pg.draw.rect(SCREEN, WHITE, [300, 200, 150, 100])
    SCREEN.blit(FONT.render("BUTTON",True,BLACK),[300,200])
    event = pg.event.poll()
    x,y = pg.mouse.get_pos()

    if (x>= 300 and x<=450 and y>=200 and y<=300) and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        text = FONT.render("Bye Bye", True, WHITE)


    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        text = FONT.render("LMB down",True, WHITE)
        print(pg.mouse.get_pos())
    elif event.type == pg.KEYDOWN and event.key == pg.K_a:
        text = FONT.render("A button down", True , WHITE)
    
    
    WINDOW.update()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            RUNNIG = False
