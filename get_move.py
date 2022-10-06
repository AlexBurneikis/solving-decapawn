from decapawn_moves import get_decapawn_moves
from minimax import minimax

def get_move(board, depth):
    legal_moves = get_decapawn_moves(board)

    best_move = legal_moves[0]
    best_score = -10

    for move in legal_moves:
        board.push(move)
        score = minimax(board, depth, -10, 10, 1)
        board.pop()

        if not board.turn:
            score *= -1

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
