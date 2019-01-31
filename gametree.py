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

        #Reached max depth: chidren = None.
        #Only calculate score of deepest layer
        if self.depth > max_depth:
            self.children = None
            #!!!!!!!!!!!!!!!!!#
            # Insert Model scoring system
            net = Net(model=model)
            vector = state(self.board).vectorizeInput()
            self.score = net.evaluateSample(vector) #return 3-bit vector (1/0,1/0,1/0)
            self.score[-1] *=-1
            self.score[-2] -=0.5
            if self.turn:
                self.score = max(self.score)
            else:
                self.score = min(self.score)
            return None
        
        self.children = []
        self.spawnChildren()

        
    # METHOD TO BE CALLED FROM HEAD NODE #
    # Searches child board configurations for their score. If white ('w'), maximize the score
    # Else if black ('b'), minimize the score.
    def evaluate(self):
        if self.children != None:
            scores = []
            for child in self.children:
                scores.append(child.evaluate())
            if self.turn:
                self.score = max(scores)
            else:
                self.score = min(scores)
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
