# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import random
import chess

def is_win(board):
    # check if a pawn has reached the opposite rank
    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}1')

        if board.piece_at(square) is None:
            continue

        if board.piece_at(square).color == chess.BLACK:
            winner = "Black"

            return winner

    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}5')

        if board.piece_at(square) is None:
            continue

        if board.piece_at(square).color == chess.WHITE:
            winner = "White"

            return winner

    if board.is_stalemate():
        if board.turn:
            winner = "Black"
        else:
            winner = "White"

        return winner

    return False

def get_legal_moves(board):
    legal_moves = [str(i) for i in board.legal_moves]

    to_remove = []
    for i in legal_moves:
        if (int(i[3]) - int(i[1])) == 2:
            to_remove.append(i)

    for i in to_remove:
        legal_moves.remove(i)

    #randomize legalMoves
    random.shuffle(legal_moves)

    return legal_moves

def evaluate(board):
    #score is number of white pawns - number of black pawns
    score = 0

    if is_win(board) == "White":
        score += 10

    if is_win(board) == "Black":
        score -= 10

    score += len(board.pieces(chess.PAWN, chess.WHITE))

    score -= len(board.pieces(chess.PAWN, chess.BLACK))

    score += (0.2 if board.turn else -0.2) * len(get_legal_moves(board))

    return score

def minimax(board, depth: int, alpha, beta, max_player):
    if depth == 0 or is_win(board):
        return evaluate(board), board

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_legal_moves(board):

            #push the move and evaluate it
            board.push_san(move)
            evaluation = minimax(board, depth - 1, alpha, beta, False)[0]
            #un-push
            board.pop()

            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

            #pruning
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

        return max_eval, best_move

    min_eval = float('inf')
    best_move = None
    for move in get_legal_moves(board):

        #push the move and evaluate it
        board.push_san(move)
        evaluation = minimax(board, depth - 1, alpha, beta, True)[0]
        #un-push
        board.pop()

        min_eval = min(min_eval, evaluation)
        if min_eval == evaluation:
            best_move = move

        #pruning
        beta = min(beta, evaluation)
        if beta <= alpha:
            break

    return min_eval, best_move

def game():
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not is_win(board):
        print(board)

        print(("White" if board.turn else "Black") + " to play.")

        move = minimax(board, 8, float("-inf"), float("inf"), board.turn)[1]

        board.push_san(str(move))

        moves.append(str(board.peek()))

    #post-game
    print(board)
    if is_win(board) == "White":
        print("White wins")
    elif is_win(board) == "Black":
        print("Black wins")
    print(moves)

game()
