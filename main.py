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

    # score += len(board.pieces(chess.PAWN, chess.WHITE))

    # score -= len(board.pieces(chess.PAWN, chess.BLACK))

    # score += (0.2 if board.turn else -0.2) * len(get_legal_moves(board))

    # #get a list of pawns
    # white_pawns = [i for i in board.pieces(chess.PAWN, chess.WHITE)]
    # black_pawns = [i for i in board.pieces(chess.PAWN, chess.BLACK)]

    # #get the distance of each pawn from the opposite side
<<<<<<< HEAD

    # white_ranks = []
    # for i in white_pawns:
    #     white_ranks.append(chess.square_rank(i)^2)

    # black_ranks = []
    # for i in black_pawns:
    #     black_ranks.append((4 - chess.square_rank(i))^2)

=======
    # white_ranks = []
    # for i in white_pawns:
    #     white_ranks.append(chess.square_rank(i)^2)

    # black_ranks = []
    # for i in black_pawns:
    #     black_ranks.append((4 - chess.square_rank(i))^2)

>>>>>>> a9286166fb0655d0477a8975c7085cb08cbe6c8a
    # score += sum(white_ranks)
    # score -= sum(black_ranks)

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
            #if beta <= alpha:
                #break

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
        #if beta <= alpha:
            #break

    return min_eval, best_move

def game():
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not is_win(board):
        print(board)

        print(("White" if board.turn else "Black") + " to play.")

<<<<<<< HEAD
        move = minimax(board, 24, float("-inf"), float("inf"), board.turn)

        print(move[0])

=======
        move = minimax(board, 6, float("-inf"), float("inf"), board.turn)

        print(move[0])

>>>>>>> a9286166fb0655d0477a8975c7085cb08cbe6c8a
        board.push_san(str(move[1]))

        moves.append(str(board.peek()))

    #post-game info
    print(board)
    if is_win(board) == "White":
        print("White wins")
    elif is_win(board) == "Black":
        print("Black wins")
    print(moves)

game()
