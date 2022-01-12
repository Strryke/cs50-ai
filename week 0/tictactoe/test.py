import tictactoe

X = "X"
O = "O"
EMPTY = None


board = [[X, X, EMPTY], [EMPTY, X, X], [X, O, X]]

# print(tictactoe.player(board))
print(tictactoe.actions(board))
# print(tictactoe.result(board, (1, 2)))
print(tictactoe.terminal(board))
print(tictactoe.winner(board))
# print(tictactoe.terminal(board))
# print(tictactoe.minimax(board))
