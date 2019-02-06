from gametree import GameTree
import random
# Player obejct interacts with gametree to navigate the gametree
class Player():
    def __init__(self):
        self.gt = GameTree(0,2)
        self.gt.scoreTree()
        
    def isClose(self,a,b):
        return abs(a-b) <= max(1e-09 * max(abs(a), abs(b)), 0.0)

    def makeMove(self):
        self.end_of_game()
        move_ind = 0
        
        print("Children: ",len(self.gt.children))
        for child_ind in range(len(self.gt.children)):
            if self.isClose(self.gt.score,self.gt.children[child_ind].score):
                move_ind = child_ind
                break

        thresh = 10
        rand = random.randint(0,100)
        if rand<thresh:
            print("Random Move Made")
            self.gt = self.gt.children[random.randint(0,len(self.gt.children)-1)]
        else:
            self.gt = self.gt.children[move_ind]
        self.gt.depth = 0
        self.gt.propogateTree()
        
    def end_of_game(self):
        if self.gt.board.is_checkmate() or self.gt.board.is_stalemate() or self.gt.board.is_insufficient_material():
            print("insufficient material")
            print(self.gt.board)
            print(self.gt.score)
            quit()

if __name__ == "__main__":
    player = Player()
    while True:
        player.makeMove()
        print(player.gt.board)
        print(player.gt.board)
        print()