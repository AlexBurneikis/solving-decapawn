from evaluate import evaluate
from decapawn_moves import get_decapawn_moves

def minimax(board, depth, alpha, beta, depth_count):
    if depth == 0 or board.is_game_over():
        return evaluate(board, depth_count)

    legal_moves = get_decapawn_moves(board)

    if board.turn:
        max_eval = -10
        for move in legal_moves:
            board.push(move)
            evaluation = minimax(board, depth - 1, alpha, beta, depth_count + 1)
            board.pop()

            max_eval = max(max_eval, evaluation)
            if max_eval >= beta:
                break
            alpha = max(alpha, evaluation)

        return max_eval
    else:
        min_eval = 10
        for move in legal_moves:
            board.push(move)
            evaluation = minimax(board, depth - 1, alpha, beta, depth_count + 1)
            board.pop()

            min_eval = min(min_eval, evaluation)
            if min_eval <= alpha:
                break
            beta = min(beta, evaluation)

        return min_eval
