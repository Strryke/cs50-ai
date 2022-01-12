"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turns = 0
    for row in board:
        for column in row:
            if column != EMPTY:
                turns += 1
    if turns % 2 == 0:
        return 0
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty = set()
    for index1, row in enumerate(board):
        for index2, column in enumerate(row):
            if column == EMPTY:
                empty.add((index1, index2))
    return empty


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")

    new_board = copy.deepcopy(board)
    symbol = player(board)
    row, column = action
    new_board[row][column] = symbol
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != None:
            return row[0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner == X or 0:
        return True
    elif actions == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner == X:
        return 1
    elif winner == 0:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        v, optimal = -math.inf, ()
        if terminal(board):
            return utility(board), optimal
        for action in actions(board):
            if (min_value(result(board, action))[0]) > v:
                v = min_value(result(board, action))[0]
                optimal = action
        return v, optimal

    def min_value(board):
        v, optimal = math.inf, ()
        if terminal(board):
            return utility(board), optimal
        for action in actions(board):
            if (max_value(result(board, action))[0]) < v:
                v = max_value(result(board, action))[0]
                optimal = action
        return v, optimal

    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
