import tensorflow as tf
import numpy as np
import copy
import chess
import pickle

archive = []
with open('dataset','rb') as f:
    archive = pickle.load(f)

# Accepts a vectorized board object as input
# Returns single numerical value which represents the favoritability of a game (+=White;-=Black)

class Model():
    def __init__(self,board_input):
        print(self.vectorizeInput(board_input.fen()))
        pass
    
    def supervised_training(self):
        pass

    # Accepts board fen
    # Returns 3D board vector
    def vectorizeInput(self,fen):
        board = fen.split(' ')[0]
        ranks = board.split('/')
        dics = {'p':0,'r':1,'n':2,'b':3,'q':4,'k':5,'P':6,'R':7,'N':8,'B':9,'Q':10,'K':11}
        vector = np.zeros([8,8,12])
        for i in range(8):
            rank = self.insertSpaces(copy.deepcopy(ranks[i]))
            for j in range(8):
                if rank[j] == str(0):
                    continue
                key = rank[j]
                ind = dics[key]
                vector[i,j,ind] = 1.
        return vector

    # Numbers in a fen represent the number of empty spaces to insert
    # Function insterSpaces(rank) handles numerical strings in fen
    def insertSpaces(self,rank):
        for i in range(len(rank)):
            try:
                space = int(rank[i])
            except Exception:
                continue
            ins = [0 for i in range(space)]
            print(rank)
            rank = np.insert(rank,[i+1 for j in range(space)],ins)
            print(rank)
            rank = np.delete(rank,i)

        print(rank)
        return rank
# dataset unzipping helper (label is last element of game)
def split_list(game):
    moves = game[:-1]
    result = game[-1]
    return moves,result
if __name__=='__main__':
# separate game moves from labels in the archive
    games = []
    labels = []
    for game in archive:
        sample,label = split_list(game)
        games.append(sample) 
        labels.append(label)

    print(games[0])


    board = chess.Board()
    m = Model(board)