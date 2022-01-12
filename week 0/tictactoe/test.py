import tictactoe

X = "X"
O = "O"
EMPTY = None


board = [[0, X, 0], [EMPTY, 0, X], [X, X, EMPTY]]

# # print(tictactoe.player(board))
# print(tictactoe.actions(board))
# # print(tictactoe.result(board, (1, 2)))
# print(tictactoe.winner(board))
# print(tictactoe.terminal(board))
print(tictactoe.minimax(board))
