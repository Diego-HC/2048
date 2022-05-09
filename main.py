import pygame as pg
import random as r

class Tile:
    def __init__(self, pos, val) -> None:
        self.val = val
        self.pos = pos
    
    def getPos(self):
        return self.pos

    def getVal(self):
        return self.val

class Board:
    def __init__(self) -> None:
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                self.board[y][x] = Tile([y, x], 0)

    def addTile(self):
        x = r.randint(0, 3)
        y = r.randint(0, 3)
        self.board[y][x] = Tile([y, x], r.choice([2, 4]))
    
    def printBoard(self):
        for y in self.board:
            for x in y:
                print('  |  ' + str(x.getVal()), end='')
            print('  |\n')

    def checkLost(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].getVal() == 0:
                    return True
        
        

if __name__ == '__main__':
    game = True
    board = Board()
    board.addTile()

    
    board.printBoard()
