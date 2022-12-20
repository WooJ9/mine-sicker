import pygame as pg
import random
import pyautogui as pa
import sys
import os

pg.init()
def resource_path(relative_path: str) -> str:
    try:
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CAPTION = "Mine-sweeper"
WIDTH = 480
HEIGHT = 510
FPS = 144
FONT = pg.font.SysFont("arial", 32, True, True)
FONT1 = pg.font.SysFont('Maplestory Bold.ttf',30)
WINDOW = pg.display
WINDOW.set_caption(CAPTION)
ICON = pg.image.load(resource_path('mine.png'))
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))
RUNNING = True
Flag = pg.image.load(resource_path('flag.png'))

RED = (255,0,0)
BLUE = (0,255,0)
BRIGHT_BLUE = (0,102,255)
BRIGHT_GREEN = (0,204,51)
BROWN = (102,51,0)
PURPLE = (102,51,153)
ORANGE = (255,102,0)
GREEN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (105,105,105)
max_mine = 40
dft = 1


class cell:
    def __init__(self,cellboard,num,x,y,x1,x2,y1,y2):
        self.boss = cellboard
        self.hasmine = False
        self.hasflag = False
        self.xcor = x
        self.ycor = y
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.cellnumber = num
        self.opened = False
        self.content = None

    def set_mine(self):
        self.hasmine = True
    
    def set_flag(self):
        self.hasflag = True
        self.boss.leftmine -= 1
    
    def unset_flag(self):
        self.hasflag = False
        self.boss.leftmine += 1
    
    def open(self):
        if self.opened == False and self.hasflag == False:
            self.opened = True
    

 


    


class board:
    def __init__(self):
        self.cellmaster = []
        for i in range(1,17):
            cellnum = 1 + 16*(i-1)
            for j in range(1,17):
                self.cellmaster.append(cell(self,cellnum,j,i,(j-1)*30,j*30,(i-1)*30+30,i*30+30))
                cellnum += cellnum

        self.leftmine = max_mine
    def num_of_mine_nearby(self):
        
        for m in self.cellmaster:
            x = m.xcor
            y = m.ycor
            X = [x-1,x,x+1]
            Y = [y-1,y,y+1]

            if m.hasmine == True:
                m.content = None
                pass
            else:
                m.content = 0

                if x-1 == 0:
                    X.remove(x-1)
                if x+1 == 17:
                    X.remove(x+1)
                if y-1 == 0:
                    Y.remove(y-1)
                if y+1 == 17:
                    Y.remove(y+1)
            
                for i in Y:
                    for j in X:
                        if  self.cellmaster[(i-1)*16 + j - 1].hasmine == True:
                            m.content = m.content + 1

                


    def with_open(self):
        for i in self.cellmaster:
            x = i.xcor
            y = i.ycor
            X = [x-1,x,x+1]
            Y = [y-1,y,y+1]
            
            if i.hasmine == True:
                pass
            else:
                if x-1 == 0:
                    X.remove(x-1)
                if x+1 == 17:
                    X.remove(x+1)
                if y-1 == 0:
                    Y.remove(y-1)
                if y+1 == 17:
                    Y.remove(y+1)
                
                if i.content == 0 and i.opened == True:
                    for c in Y:
                        for j in X:
                            self.cellmaster[(c-1)*16 + j - 1].opened = True

                

    def random_mine_generate(self):
        self.minemaster = []

        while True:
            a = random.randrange(1,257)
            if a not in self.minemaster:
                self.minemaster.append(a)
                self.cellmaster[a-1].set_mine()
            if len(self.minemaster) == 40:
                break

    
    def render(self):
        MINE_TEXT = FONT1.render("Mine Left: %d" % self.leftmine, True, BLACK)
        SCREEN.blit(MINE_TEXT,(10,10))
        self.with_open()

        for j in self.cellmaster:
            if j.hasflag == True:
                SCREEN.blit(Flag,[j.x1,j.y1])
            else:
                pg.draw.rect(SCREEN,BLACK,[j.x1,j.y1,30,30],2)
        for j in self.cellmaster:
            if j.opened == True:
                pg.draw.rect(SCREEN,WHITE,[j.x1,j.y1,30,30])
                pg.draw.rect(SCREEN,BLACK,[j.x1,j.y1,30,30],2)

        self.num_of_mine_nearby()

        for i in self.cellmaster:
            if i.opened == True:

                if i.content == 0:
                    Text_0 = FONT1.render("0",True,BRIGHT_BLUE)
                    SCREEN.blit(Text_0,[i.x1+10,i.y1+10])
                if i.content == 1:
                    Text_1 = FONT1.render("1",True,BRIGHT_BLUE)
                    SCREEN.blit(Text_1,[i.x1+10,i.y1+10])
                if i.content == 2:
                    Text_2 = FONT1.render("2",True,BRIGHT_GREEN)
                    SCREEN.blit(Text_2,[i.x1+10,i.y1+10])            
                if i.content == 3:
                    Text_3 = FONT1.render("3",True,RED)
                    SCREEN.blit(Text_3,[i.x1+10,i.y1+10])
                if i.content == 4:
                    Text_4 = FONT1.render("4",True,BLUE)
                    SCREEN.blit(Text_4,[i.x1+10,i.y1+10])
                if i.content == 5:
                    Text_5 = FONT1.render("5",True,BROWN)
                    SCREEN.blit(Text_5,[i.x1+10,i.y1+10])
                if i.content == 6:
                    Text_6 = FONT1.render("6",True,GREEN)
                    SCREEN.blit(Text_6,[i.x1+10,i.y1+10])
                if i.content == 7:
                    Text_7 = FONT1.render("7",True,PURPLE)
                    SCREEN.blit(Text_7,[i.x1+10,i.y1+10])            
                if i.content == 8:
                    Text_8 = FONT1.render("8",True,ORANGE)
                    SCREEN.blit(Text_8,[i.x1+10,i.y1+10])
        for i in self.cellmaster:
            if i.opened == True and i.hasmine == True:
                for j in self.minemaster:
                    SCREEN.blit(ICON,[self.cellmaster[j-1].x1,self.cellmaster[j-1].y1])


    def defeat(self):
        for i in self.cellmaster:
            if i.opened == True and i.hasmine == True:
                pa.confirm(text='YOU touch the mine. Try again?', title='GAME OVER',buttons=['OK','Cancel'])


def SCREEN_fill():
    SCREEN.fill(GRAY)



def cellnumber():
    a,b = mouse_position()

    A = a // 30
    if b < 30:
        return 0
    else:
        B = b // 30
        return A + (B-1)*16 + 1










def mouse_position():
    return pg.mouse.get_pos()

game_board = board()
game_board.random_mine_generate()
print(game_board.minemaster)



while RUNNING:
    pg.time.Clock().tick(FPS)
    SCREEN_fill()
    game_board.render()


    WINDOW.update()

    for event in pg.event.get():
        
        current_cellnum = cellnumber()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            
            if current_cellnum == 0:
                pass
            if game_board.cellmaster[current_cellnum-1].opened == True and game_board.cellmaster[current_cellnum-1].hasflag == False:
                    pass
            elif game_board.cellmaster[current_cellnum-1].hasflag == False:
                game_board.cellmaster[current_cellnum-1].set_flag()
                
            else:
                game_board.cellmaster[current_cellnum-1].unset_flag()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            

            if current_cellnum == 0:
                pass
            elif game_board.cellmaster[current_cellnum-1].hasflag == True:
                pass
            elif game_board.cellmaster[current_cellnum-1].opened == False:
                game_board.cellmaster[current_cellnum-1].open()
            
            
            game_board.defeat()
        if event.type == pg.QUIT:
            WINDOW.quit()
            RUNNING = False
