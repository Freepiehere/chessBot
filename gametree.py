import chess
import time
import numpy as np
import random
from net import Net

class GameTree():
    def __init__(self,depth,max_depth,board=None):
        self.depth = depth  
        self.max_depth = max_depth
        self.children = []
        if board:
            self.board = board
        else:
            self.board = chess.Board()
        
        self.propogateTree()

    def chooseScore(self,board_score):
        if self.board.turn:
            return max(board_score)
        return min(board_score)

    def scoreTree(self):
        #something wrong with scoring system.
        #Isn't the parent supposed to inherit score from the children
        #And rethink the whole subracting half and multiplying by -1 crap.
        #relate the score of the node to the INDEX of the max number found in the net output

    def checkDepth(self):
        if self.depth>self.max_depth:
            return True
        return False

    def setDepth(self,depth):
        self.depth = depth
        for child in self.children:
            child.setDepth(depth+1)
    
    def propogateTree(self):
        if self.checkDepth():
            return None
        elif not self.children:
            self.spawnChildren()
        else:
            for child in self.children:
                child.propogateTree()
        
    # Accepts chess board object and populates children field with legal board configurations
    def spawnChildren(self):
        for move in self.board.legal_moves:
            next_board = chess.Board()
            next_board.set_fen(self.board.fen())
            move = chess.Move.uci(move)
            next_board.push(chess.Move.from_uci(move))
            self.children.append(GameTree(self.depth+1,self.max_depth,next_board))

max_depth = 2

def initialize(max_depth=max_depth,starting_board=None):
    depth = 0
    gt = GameTree(depth,max_depth)
    return gt

def loadModel(filename = "model.json"):
    import keras
    json_file = open("model.json","r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    return loaded_model

model = loadModel()
net = Net(model=model)

if __name__ == '__main__':
    print('GameTree main')
    depth = 0
    board =chess.Board()

    tik = time.time()
    gt = GameTree(depth,max_depth)
    tok = time.time()
    print('Time to initiate: %f' % (tok-tik))

    tik = time.time()
    gt.scoreTree()
    tok = time.time()
    print('Time to score: %f' % (tok-tik))

    while gt.children:
        print(gt.board)
        print(gt.score)
        print()
        gt = gt.children[0]
