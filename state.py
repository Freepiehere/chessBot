import copy
import chess

#archive = []
#with open('dataset','rb') as f:
#    archive = pickle.load(f)

# Accepts a vectorized board object as input
# Returns single numerical value which represents the favoritability of a game (+=White;-=Black)

class State(object):
    def __init__(self,board=None):
        if board:
            self.board = board
        else:
            self.board = chess.Board()
        
    # Accepts board fen
    # Returns 3D board vector
    def vectorizeInput(self):
        import numpy as np
        fen = self.board.fen()
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
        return vector.flatten()

    # Numbers in a fen represent the number of empty spaces to insert
    # Function insterSpaces(rank) handles numerical strings in fen
    def insertSpaces(self,rank):
        rank_prime = ""
        for c in rank:
            try:
                for i in range(int(c)):
                    rank_prime+=(str(0))
            except Exception:
                rank_prime+=(c)
        return rank_prime

# dataset unzipping helper (label is last element of game)
def split_list(game):
    moves = game[:-1]
    result = game[-1]
    return moves,result

#if __name__=='__main__':
# separate game moves from labels in the archive
#    games = []
#    labels = []
#    for game in archive:
#        sample,label = split_list(game)
#        games.append(sample) 
 #       labels.append(label)
#
#    m = State()