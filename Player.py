<<<<<<< HEAD
import numpy
import chess
import GameTree
import Model

# Player object decided upon what moves to make given a GameTree object and whichever team the player is controlling,
# either white ('w') or black ('b')
class Player():
    def __init__(self,gt,team):
        self.gt = gt
        self.color = team
        pass
    
    # function "evaluate" will traverse the GameTree object searching for the most logical game branch to pursue
    # determined from a Mini/Maxi logical search algorithm.
    def evaluate(self,gt):
        
        pass

if __name__=="__main__":
    starting_gt = GameTree.initialize(None)
=======
import numpy
import chess
import GameTree
import Model

# Player object decided upon what moves to make given a GameTree object and whichever team the player is controlling,
# either white ('w') or black ('b')
class Player():
    def __init__(self,gt,team):
        self.gt = gt
        self.color = team
        pass
    
    # function "evaluate" will traverse the GameTree object searching for the most logical game branch to pursue
    # determined from a Mini/Maxi logical search algorithm.
    def evaluate(self,gt):
        
        pass

if __name__=="__main__":
    starting_gt = GameTree.initialize(None)
>>>>>>> 7dac61262ee93e0fcb202ca1c38ed759a5031bd6
    player = Player(starting_gt,'w')