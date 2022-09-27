# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import random
import chess

def is_win(board):
    #determine who has won or if no one has

    #check if a pawn has reached the opposite rank
    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}1')

        if board.piece_at(square) is None:
            continue

        if board.piece_at(square).color == chess.BLACK:
            return "Black"

    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}5')

        if board.piece_at(square) is None:
            continue

        if board.piece_at(square).color == chess.WHITE:
            return "White"

    #whoever cant play loses
    if board.is_stalemate():
        if board.turn:
            return "Black"
        return "White"

    return False

def get_legal_moves(board):
    #get legal moves without pawns moving two spaces
    #shuffle the legal moves
    legal_moves = [str(i) for i in board.legal_moves]

    #get the moves to remove
    to_remove = []
    for i in legal_moves:
        if (int(i[3]) - int(i[1])) == 2:
            to_remove.append(i)

    #remove them
    for i in to_remove:
        legal_moves.remove(i)

    #randomize legalMoves - (otherwise same game every time)
    random.shuffle(legal_moves)

    return legal_moves

def evaluate(board):
    score = 0

    if is_win(board) == "White":
        score += 1

    if is_win(board) == "Black":
        score -= 1

    return score

def minimax(board, depth, alpha, beta, max_player):
    if depth == 0 or is_win(board):
        return evaluate(board)

    if max_player:
        max_eval = float('-inf')
        for move in get_legal_moves(board):
            board.push_san(move)
            evaluation = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval

    min_eval = float('inf')
    for move in get_legal_moves(board):
        board.push_san(move)
        evaluation = minimax(board, depth - 1, alpha, beta, True)
        board.pop()
        min_eval = min(min_eval, evaluation)
        beta = min(beta, evaluation)
        if beta <= alpha:
            break
    return min_eval

def get_move(board, depth):
    #for all the legalMoves get the one with best minimax
    #return the best move

    legalMoves = get_legal_moves(board)

    bestMove = legalMoves[0]

    bestScore = float('-inf')

    for move in legalMoves:
        board.push_san(move)
        score = minimax(board, depth, float('-inf'), float('inf'), False)
        board.pop()

        if abs(score) > bestScore:
            bestScore = score
            bestMove = move

    return bestScore, bestMove

def minimax_chess(board, depth: int, alpha, beta, max_player):
    if depth == 0 or is_win(board):
        return evaluate(board), board

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_legal_moves(board):

            #push the move and evaluate it
            board.push_san(move)
            evaluation = minimax_chess(board, depth - 1, alpha, beta, False)[0]
            #un-push
            board.pop()

            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

            #pruning
            if beta <= alpha:
                break

            alpha = max(alpha, evaluation)

        return max_eval, best_move

    min_eval = float('inf')
    best_move = None
    for move in get_legal_moves(board):

        #push the move and evaluate it
        board.push_san(move)
        evaluation = minimax_chess(board, depth - 1, alpha, beta, True)[0]
        #un-push
        board.pop()

        min_eval = min(min_eval, evaluation)
        if min_eval == evaluation:
            best_move = move

        #pruning
        if beta <= alpha:
            break

        beta = min(beta, evaluation)

    return min_eval, best_move

def game():
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []
    evals = []

    while not is_win(board):
        print(board)

        print(("White" if board.turn else "Black") + " to play.")

        move = get_move(board, 10)

        print(move[0])
        evals.append(move[0])

        board.push_san(str(move[1]))

        moves.append(str(board.peek()))

    #post-game info
    print(board)
    if is_win(board) == "White":
        print("White wins")
    elif is_win(board) == "Black":
        print("Black wins")
    print(moves)
    print(evals)

game()
