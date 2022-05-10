import pygame as pg
import random as r
import sys

class Tile:
    def __init__(self, pos, val) -> None:
        self.val = val
        self.pos = pos
    
    def getPos(self):
        return self.pos

    def getVal(self):
        return self.val

    def setPos(self, pos):
        self.pos = pos

    def setVal(self, val):
        self.val = val

    def drawTile(self, screen):
        if self.val != 0:
            tileRect = pg.draw.rect(screen, [255, 255, 0], pg.Rect(self.pos[1] * 180, self.pos[0] * 180, 180, 180))
            # pg.draw.rect(screen, [255, 255, 0], pg.Rect(self.pos[1] * 180, self.pos[0] * 180, 180, 180))
            text_surface_object = pg.font.SysFont('comicsans', 30).render(
                        str(self.val), True, [0, 0, 0]
                    )
            text_rect = text_surface_object.get_rect(center=tileRect.center)
            screen.blit(text_surface_object, text_rect)
            pg.display.flip()
    

class Board:
    def __init__(self, screen) -> None:
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                self.board[y][x] = Tile([y, x], 0)

        self.screen = screen

    def addTile(self):
        while True:    
            x = r.randint(0, 3)
            y = r.randint(0, 3)
            if self.board[y][x].getVal() == 0:
                self.board[y][x] = Tile([y, x], r.choice([2, 4]))
                break
        
    def printBoard(self):
        for y in self.board:
            for x in y:
                print('  |  ' + str(x.getVal()), end='')
            print('  |\n')

    def drawBoard(self):
        for y in self.board:
            for x in y:
                x.drawTile(self.screen)

    def checkLost(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].getVal() == 0:
                    return True

        for y in range(len(self.board) - 1):
            for x in range(len(self.board[y]) - 1):
                if self.board[y][x].getVal() == self.board[y + 1][x].getVal() or self.board[y][x].getVal() == self.board[y][x + 1].getVal(): 
                    return True

    def movement(self, move):
        mergeBoard = [
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True]
        ]

        continueMove = 2

        while continueMove != 0:
            if move == 'w':
                for y in range(1, len(self.board)):
                    for x in range(len(self.board[y])):
                        if self.board[y - 1][x].getVal() == 0 and self.board[y][x].getVal() != 0:
                            self.board[y - 1][x].setVal(self.board[y][x].getVal())
                            self.board[y][x].setVal(0)
                            continueMove = 2

                        elif self.board[y][x].getVal() != 0 and (mergeBoard[y - 1][x] == True) and (mergeBoard[y][x] == True) and (self.board[y - 1][x].getVal() == self.board[y][x].getVal()):
                            self.board[y - 1][x].setVal(self.board[y - 1][x].getVal() * 2)
                            self.board[y][x].setVal(0)
                            mergeBoard[y - 1][x] = False
                            mergeBoard[y][x] = False
                            continueMove = 2

                continueMove -= 1
            
            if move == 's':
                for y in range(len(self.board) - 2, -1, -1):
                    for x in range(len(self.board[y])):
                        if self.board[y + 1][x].getVal() == 0 and self.board[y][x].getVal() != 0:
                            self.board[y + 1][x].setVal(self.board[y][x].getVal())
                            #self.board[y][x].setVal(0)
                            continueMove = 2

                        elif self.board[y][x].getVal() != 0 and (mergeBoard[y + 1][x] == True) and (mergeBoard[y][x] == True) and (self.board[y + 1][x].getVal() == self.board[y][x].getVal()):
                            self.board[y + 1][x].setVal(self.board[y + 1][x].getVal() * 2)
                            self.board[y][x].setVal(0)
                            mergeBoard[y + 1][x] = False
                            #mergeBoard[y][x] = False
                            continueMove = 2

                continueMove -= 1

            if move == 'a':
                for y in range(len(self.board)):
                    for x in range(1, len(self.board[y])):
                        if self.board[y][x - 1].getVal() == 0 and self.board[y][x].getVal() != 0:
                            self.board[y][x - 1].setVal(self.board[y][x].getVal())
                            #self.board[y][x].setVal(0)
                            continueMove = 2

                        elif self.board[y][x].getVal() != 0 and (mergeBoard[y][x - 1] == True) and (mergeBoard[y][x] == True) and (self.board[y][x - 1].getVal() == self.board[y][x].getVal()):
                            self.board[y][x - 1].setVal(self.board[y][x].getVal() * 2)
                            self.board[y][x].setVal(0)
                            mergeBoard[y][x - 1] = False
                            #mergeBoard[y][x] = False
                            continueMove = 2

                continueMove -= 1

            if move == 'd':
                for y in range(len(self.board)):
                    for x in range(len(self.board[y]) - 2, -1, -1):
                        if self.board[y][x + 1].getVal() == 0 and self.board[y][x].getVal() != 0:
                            self.board[y][x + 1].setVal(self.board[y][x].getVal())
                            self.board[y][x].setVal(0)
                            continueMove = 2

                        elif self.board[y][x].getVal() != 0 and (mergeBoard[y][x + 1] == True) and (mergeBoard[y][x] == True) and (self.board[y][x + 1].getVal() == self.board[y][x].getVal()):
                            self.board[y][x + 1].setVal(self.board[y][x + 1].getVal() * 2)
                            self.board[y][x].setVal(0)
                            mergeBoard[y][x + 1] = False
                            #mergeBoard[y][x] = False
                            continueMove = 2

                continueMove -= 1

                    

if __name__ == '__main__':
    pg.init()
    size = width, height = 720, 720
    speed = [0, 1]
    grey = [47, 79, 79]
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    game = True
    board = Board(screen)
    board.addTile()
    screen.fill(grey)
    board.drawBoard()
    pg.display.flip()

    while game:

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    board.movement('d')
                    board.addTile()
                    screen.fill(grey)
                    board.drawBoard()
                    pg.display.flip()
                    game = board.checkLost()

                if event.key == pg.K_LEFT:
                    board.movement('a')
                    board.addTile()
                    screen.fill(grey)
                    board.drawBoard()
                    pg.display.flip()
                    game = board.checkLost()

                if event.key == pg.K_UP:
                    board.movement('w')
                    board.addTile()
                    screen.fill(grey)
                    board.drawBoard()
                    pg.display.flip()
                    game = board.checkLost()


                if event.key == pg.K_DOWN:
                    board.movement('s')
                    board.addTile()
                    screen.fill(grey)
                    board.drawBoard()
                    pg.display.flip()
                    game = board.checkLost()

        clock.tick(30)
