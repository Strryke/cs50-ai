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
        return X
    else:
        return O


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

    new_board = copy.deepcopy(board)
    symbol = player(board)
    row, column = action
    if board[row][column] != EMPTY:
        raise Exception("Invalid Action")
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
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]

    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win_player = winner(board)

    if win_player == X or win_player == O:
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
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
