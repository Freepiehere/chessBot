import chess
import time
import numpy as np
import state
import random
class GameTree():
    def __init__(self,depth,max_depth,board=None,gt=None):
        self.depth = depth
        self.max_depth = max_depth

        #Reached max depth: chidren = None.
        #Only calculate score of deepest layer
        if self.depth > max_depth:
            self.children = None
            #!!!!!!!!!!!!!!!!!#
            # Insert Model scoring system
            self.score = random.randint(-100,100)
            return None

        # Construct Game Tree
        if gt:
            for child in gt.children:
                GameTree(depth+1,max_depth,None,child)
        elif board:
            self.board = board
        else:
            self.board = chess.Board()
        
        #True: white; False: black
        self.turn = self.board.turn
        
        self.children = []
        self.spawnChildren()
        self.evaluate()
        
    # Searches child board configurations for their score. If white ('w'), maximize the score
    # Else if black ('b'), minimize the score.
    def evaluate(self):
        pass

    # Accepts chess board object and populates children field with legal board configurations
    def spawnChildren(self):
        for move in self.board.legal_moves:
            next_board = chess.Board()
            next_board.set_fen(self.board.fen())
            move = chess.Move.uci(move)
            next_board.push(chess.Move.from_uci(move))
            self.children.append(GameTree(self.depth+1,self.max_depth,next_board))

max_depth = 2

def initialize(max_depth=max_depth,starting_board=None,starting_gt=None):
    depth = 0
    gt = GameTree(depth,max_depth,starting_board,starting_gt)
    return gt

if __name__ == '__main__':
    print('GameTree main')
    depth = 0
    tik = time.time()
    gt = initialize()
    tok = time.time()
    while gt.children:
        print(gt.board)
        gt = gt.children[-1]
    print(tok-tik)
