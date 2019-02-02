from gametree import GameTree
import random
# Player obejct interacts with gametree to navigate the gametree
class Player():
    def __init__(self,team,opponent=None,gt=None):
        if not gt:
            print('make new gametree')
            self.gt = GameTree(depth=0,max_depth=2)
        else:
            self.gt = gt
        self.team = team
        
        self.opponent = opponent
        if not opponent:
            self.opponent = Player(not self.team,opponent=self,gt=self.gt)
        
    def makeMove(self):
        print('evaluate gametree')
        self.gt.evaluate()
        print(self.gt.board)
        print(self.gt.score)
        print()

        move_scores = []
        child_index = 0
        for child in self.gt.children:
            move_scores.append(child.score)
        if self.team:
            child_index = move_scores.index(max(move_scores))
        else:
            child_index = move_scores.index(min(move_scores))
        rand = random.randint(0,100)
        thresh = 20
        # thresh* percent change a random move is made
        # avoids the same game being played
        if rand < thresh:
            self.opponent.gt = GameTree(depth=0,max_depth=2,gt=self.gt.children[random.randint(0,len(self.gt.children)-1)])        
        else:
            self.opponent.gt = GameTree(depth=0,max_depth=2,gt=self.gt.children[child_index])
        self.passTurn()
    
    def passTurn(self):
        if self.gt.board.is_checkmate():
            self.end_of_game()
        self.opponent.makeMove()

    def end_of_game(self):
        print(self.gt.board)
        quit()

if __name__ == "__main__":
    print('begin')
    gt = GameTree(depth=0,max_depth=2)
    print('make player')
    player1 = Player(gt.turn)
    print("begin game")        
    player1.makeMove()