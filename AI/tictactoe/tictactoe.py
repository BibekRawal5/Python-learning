"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    
    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i,j
    available = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available.append((i,j))

    return available

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = board.copy()
    i,j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    WINING_SET = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)], [(2,0),(1,1),(0,2)]
        ]
    
    while True:
        for aset in WINING_SET:
            sum_x = 0
            sum_o = 0
            for tup in aset:
                i,j = tup
                if board[i][j] == X:
                    sum_x += 1
                elif board[i][j] == O:
                    sum_o += 1 
            if sum_x == 3:
                return X
            elif sum_o == 3:
                return O
        
        return None
                    
                    
                    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    status = winner(board)
    if status == X or status == O:
        return True
    
    for row in board:
        if row.count(EMPTY):
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    status = winner(board)
    if status == X:
        return 1
    elif status == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

