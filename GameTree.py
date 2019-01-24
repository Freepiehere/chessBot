import chess
import time
import numpy as np

import random
class GameTree():
    def __init__(self,depth,max_depth,parent,board=None,gt=None):
        self.parent = parent
        if not self.parent:
            self.turn = 'w'
        elif self.parent.turn == 'b':
            self.turn = 'w'
        else:
            self.turn = 'b'

        #!!!!!!!!!!!!!!!!!#
        # Insert Model scoring system
        self.score = random.randint(-100,100)
        
        self.depth = depth
        self.max_depth = max_depth
        
        if self.depth == max_depth:
            self.children = None
            return None
        if gt:
            for child in gt.children:
                GameTree(depth+1,max_depth,child)
        elif board:
            self.board = board
        else:
            self.board = chess.Board()

        self.children = []
        self.spawnChildren()
        self.evaluate()
        
    # Searches child board configurations for their score. If white ('w'), maximize the score
    # Else if black ('b'), minimize the score.
    def evaluate(self):
        if self.turn == 'w':
            m = True
            score = -100
        else:
            m = False
            score = 100
        if m:
            for child in self.children:
                if child.score > score:
                    score = child.score
        else:
            for child in self.children:
                if child.score < score:
                    score = child.score
        self.score = score

    # Accepts chess board object and populates children field with legal board configurations
    def spawnChildren(self):
        for move in self.board.legal_moves:
            next_board = chess.Board()
            next_board.set_fen(self.board.fen())
            move = chess.Move.uci(move)
            next_board.push(chess.Move.from_uci(move))
            self.children.append(GameTree(self.depth+1,self.max_depth,self,next_board))
            
def initialize(starting_board=None):
    depth = 0
    gt = GameTree(depth,max_depth,None)
    return gt

max_depth = 3
if __name__ == '__main__':
    print('GameTree main')
    depth = 0
    tik = time.time()
    gt = initialize()
    tok = time.time()
    while gt.children:
        print(gt.score)
        gt = gt.children[-1]
    print(tok-tik)
