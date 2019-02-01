from gametree import GameTree

# Player obejct interacts with gametree to navigate the gametree
class Player():
    def __init__(self,team,gt=None):
        if not gt:
            print('make new gametree')
            self.gt = GameTree(depth=0,max_depth=2)
        else:
            self.gt = gt
        if not team:
            self.team = gt.turn
        else:
            self.team = team
        print('evaluate gametree')
        self.gt.evaluate()
        
    def makeMove(self):
        move_scores = []
        child_index = 0
        for child in self.gt.children:
            move_scores.append(child.score)

        if self.team:
            child_index = move_scores.index(max(move_scores))
        else:
            child_index = move_scores.index(min(move_scores))
        quit()
        self.gt = GameTree(depth=0,max_depth=2,gt=self.gt.children[child])
        self.gt.evaluate()

if __name__ == "__main__":
    print('begin')
    gt = GameTree(depth=0,max_depth=2)
    print('make player')
    player = Player(gt.turn)
    while not gt.board.is_checkmate():
        print(player.gt.board)
        player.makeMove()
        gt = player.gt
        player = Player(team=gt.turn,gt=gt)
        