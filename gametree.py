import chess
import time
import numpy as np
import random
from net import Net
from state import state

class GameTree():
    def __init__(self,depth,max_depth,board=None,gt=None):
        self.depth = depth
        self.max_depth = max_depth

        if gt:
            self.children = gt.children
            self.board = gt.board
        elif board:
            self.children = None
            self.board = board
        else:
            self.children = None
            self.board = chess.Board()
        self.turn = self.board.turn
        
        if self.depth > self.max_depth:
            self.terminateTree(self)
            return None
        
        if not self.children:
            self.newLayer(self)
        else:
            for child in self.children:
                self.propogateTree(child)
    
    def propogateTree(self,gt):
        gt.depth = self.depth+1
        if gt.depth > self.max_depth:
            self.terminateTree(gt)
            return None
        if not gt.children:
            self.newLayer(gt)
    
    def newLayer(self,gt):
        gt.children = []
        gt.spawnChildren()
    
    def terminateTree(self,gt):
        gt.children = None
        sample = state(self.board).vectorizeInput()
        self.score = net.evaluateSample(sample)
        self.score[-2] -= 0.5
        self.score[-1] *= -1.

    # METHOD TO BE CALLED FROM HEAD NODE #
    # Searches child board configurations for their score. If white ('w'), maximize the score
    # Else if black ('b'), minimize the score.
    def evaluate(self):
        if not self.children:
            scores = self.score
        else:
            scores = []
            for child in self.children:
                scores.append(child.evaluate())
        if self.turn:
            try:
                self.score = max(scores)
            except Exception:
                self.score = scores
        else:
            try:
                self.score = min(scores)
            except Exception:
                self.score = scores
        
        return self.score
        

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
    tik = time.time()
    gt = initialize()
    tok = time.time()
    print("Time to initialize: %f" % (tok-tik))
    tik=time.time()
    gt_score = gt.evaluate()
    tok=time.time()
    print(gt_score)
    print("Time to traverse: %f" % (tok-tik))
