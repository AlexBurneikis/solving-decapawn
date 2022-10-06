from decapawn_win import is_win

def evaluate(board, depth):
    if is_win(board):
        return -1/(depth) if board.turn else 1/(depth)
    return 0