from gametree import GameTree
import random
# Player obejct interacts with gametree to navigate the gametree
class Player():
    def __init__(self):
        self.gt = GameTree(0,2)
        self.gt.scoreTree()
        
    
    def makeMove(self):
        self.end_of_game()
        for child_ind in range(len(self.gt.children)):
            score = self.gt.children[child_ind].score
            if score == self.gt.score:
                move_ind = child_ind
                break

        thresh = 20
        rand = random.randint(0,100)
        if rand<thresh:
            self.gt = self.gt.children[random.randint(0,len(self.gt.child_scores)-1)]
        else:
            self.gt = self.gt.children[move_ind]
        
    def end_of_game(self):
        if self.gt.board.is_checkmate() or self.gt.board.is_stalemate():
            print(self.gt.board)
            print(self.gt.score)
            quit()

if __name__ == "__main__":
    player = Player()
    while True:
        player.makeMove()