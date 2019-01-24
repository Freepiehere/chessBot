<<<<<<< HEAD
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
	optimizer. 

Section 2:

The Data: 
Format:

# 1.t 2.date 3.result 4.welo 5.belo 
# 6.len 7.date_c 8.resu_c 9.welo_c 
# 10.belo_c 11.edate_c 12.setup 13.fen 14.resu2_c 
# 15.oyrange 16.bad_len 17.game...

-1 2000.03.14 1-0 2851 None 67 date_false result_false welo_false belo_true edate_true 
	setup_false fen_false result2_false oyrange_false blen_false ###

-(W)(#move).(to_tile)(/+) (B)(#move).(to_tile)(/+)
	+ = "Check"

0/1;0/63;0/1; bits of data (W/B)(a1/h8)(not/check)

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
=======
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
	optimizer. 

Section 2:

The Data: 
Format:

# 1.t 2.date 3.result 4.welo 5.belo 
# 6.len 7.date_c 8.resu_c 9.welo_c 
# 10.belo_c 11.edate_c 12.setup 13.fen 14.resu2_c 
# 15.oyrange 16.bad_len 17.game...

-1 2000.03.14 1-0 2851 None 67 date_false result_false welo_false belo_true edate_true 
	setup_false fen_false result2_false oyrange_false blen_false ###

-(W)(#move).(to_tile)(/+) (B)(#move).(to_tile)(/+)
	+ = "Check"

0/1;0/63;0/1; bits of data (W/B)(a1/h8)(not/check)

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
>>>>>>> 7dac61262ee93e0fcb202ca1c38ed759a5031bd6
		-Else the GameTree is completed to the max depth