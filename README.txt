 * Introduction:

Section 1:

The Goal: The creation of a program capable of 
playing chess to such a degree to surmount myself.

-Using a heuristical methodology, chess moves will be chosen from all possible
	moves, explored to a feasible depth. Board configurations will be scored based
	upon a number of board features. A board's score (s) will start as a linear
	combination of all elements comprising a feature set (X). i.e.,
	
	s = x_1*a_1 + x_2*a_2 + x_3*a_3 + ... + x_n*a_n, s.t. n is an index of ||X||,
							and a_n is the nth coefficient of x.

-The values comprising the weight set (a) will be calculated by a machine learning 
	optimizer ot allow further abstraction of the model.

Section 2:

The Data: 
Format:
pgn chess format, compressed chess game dataset.
Vecotrization:
the board may be represented and a 768 bit vector; 64squares*6pieces*2teams

 * Requirements:
-Heuristic game exploration algorithm.
	-Exploring as many possible games as possible.
	-Choose the board of highest feasible score.
		-Assuming opponent will play "perfectly"

-Board scoring algorithm.
	-Based in machine learning coefficient estimator.
	-coefficients of board features calculate board score.

-A chess interface (pychess?).
	- the algorithm may pull possible moves.
		-stored to datastructure.

-A data parser for a text-based database file.
	-Format shown above in sec 2.

* GameTree:
-Accepts current depth, max depth, current board cinfiguration (default None), 
	and a GameTree object (default None)
-Recursively builds game tree to a specified max depth
-If board configuration is supplied, a new GameTree node is created and recursive
	construction is continued.
-If GameTree node is supplied, tree is traversed to the lowest completed layer.
	-If lowest completed layer is the max depth, no action is taken
		-Else the GameTree is completed to the max depth

* State:
-Represents a given chess board configuration in a 768bit vector
-State inherits the object function. Accepts a chess.Board() object (default, None))

* net: