# Data Parser
#
# program will parse through a text-based dataset file and save the
# organized data into a numpy file.

# 1.t 2.date 3.result 4.welo 5.belo 
# 6.len 7.date_c 8.resu_c 9.welo_c 
# 10.belo_c 11.edate_c 12.setup 13.fen 14.resu2_c 
# 15.oyrange 16.bad_len 17.game...
import numpy as np
import csv
import pickle

filename = 'games.csv'
def main(filename):
    archive = []
    if filename[-3:] == 'txt':
        with open(filename,'r') as data:
            archive = buildData(data)
            print(archive[0:5])
    elif filename[-3:] == 'csv':
        with open(filename,newline='') as csvfile:
            spamreader = csv.reader(csvfile,quotechar='|')
            next(spamreader)
            win_id = {'white':1.,'draw':0.5,'black':-1}
            for row in spamreader:
                moves = row[12].split(' ')
                moves.append(win_id[row[6]])
                archive.append(moves)
        with open('dataset','wb') as f:
            pickle.dump(archive,f)

    #np.save('chess_Dataset.npy',archive)

def buildData(data):
    games = data.readlines()
    archive = gameParser(games)
    return archive

#Accepts dataset string (ds)
#isolates all games of the dataset.
def gameParser(catalog):
    games = []
    start_line = 5
    catalog = catalog[start_line:]
    for game in catalog:
        stats,moves = moveParser(game)
        stats.extend(moves)
        games.append(stats)
    return games

#isolates all moves in a game
# Accepts game string (gs)
# Returns index, 
def moveParser(gs):
    moves = []
    game_num = gs[0]
    result = gs[2]
    num_moves = gs[5]
    start_ind = 17
    moves = gs.split(' ')[start_ind:-1]
    return [game_num,result,num_moves],[moves]
    
if __name__ == "__main__":
    main(filename)
    # Path:
    # D:\Coding\Chessbot