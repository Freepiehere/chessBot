import chess.pgn
import numpy as np
import os
import io
from state import State

# Accepts directory contianing datset files
def get_dataset(directory,num_samples=None):
    X,Y = [],[]
    result_key = {'1-0':np.array([1.,0.,0.]),'1/2-1/2':np.array([0.,1.,0.]),'0-1':np.array([0.,0.,1.])}
    for filename in os.listdir(directory):
        filename = os.fsdecode(filename)
        if not filename.endswith('.pgn'):
            continue

        gameInd = 0
        pgn = open(directory+"/"+filename)
        while 1:
            
            game = chess.pgn.read_game(pgn)
            if not game:
                break

            moves = game.mainline_moves()
            board = chess.Board()
            result = game.headers['Result']

            for _,move in enumerate(moves):
                board.push(move)
                ser = State(board).vectorizeInput()
                X.append(ser)
                Y.append(result_key[result])

            if len(X) > num_samples:
                return np.array(X),np.array(Y)
            gameInd += 1
            print("Parsing game %d and got %d samples" % (gameInd,len(X)))
    X=np.array(X)
    Y=np.array(Y)
    return X,Y
if __name__ == "__main__":
    X,Y=get_dataset("KingBase2019-pgn",500000)
    print(X.shape,Y.shape)
    np.savez('dataset.npz',X,Y)
    