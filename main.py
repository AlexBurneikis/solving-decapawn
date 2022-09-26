import random
import chess

def isWin(board):
    # check if a pawn has reached the opposite rank
    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}1')

        if board.piece_at(square) == None:
            continue

        if board.piece_at(square).color == chess.BLACK:
            winner = "Black"
            
            return winner

    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}5')

        if board.piece_at(square) == None:
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

def generateLegalMoves(board):
    legalMoves = [str(i) for i in board.legal_moves]
    
    toRemove = []
    for i in legalMoves:
        if (int(i[3]) - int(i[1])) == 2:
            toRemove.append(i)

    for i in toRemove:
        legalMoves.remove(i)

    #randomize legalMoves
    random.shuffle(legalMoves)

    return legalMoves  

def evaluate(board):
    #score is number of white pawns - number of black pawns
    score = 0
    
    if isWin(board) == "White":
        return 100

    if isWin(board) == "Black":
        return -100

    for i in board.pieces(chess.PAWN, chess.WHITE):
        score += 1

    for i in board.pieces(chess.PAWN, chess.BLACK):
        score -= 1

    return score

def max(score, bestScore):
    if score > bestScore:
        return score
    return bestScore

def min(score, bestScore):
    if score < bestScore:
        return score
    return bestScore

def minimax(board, depth, alpha, beta, maxPlayer):
    if depth == 0 or isWin(board):
        return evaluate(board), board

    if maxPlayer:
        maxEval = float('-inf')
        best_move = None
        for move in generateLegalMoves(board):
            board.push_san(move)
            evaluation = minimax(board, depth - 1, alpha, beta, False)[0]
            board.pop()
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in generateLegalMoves(board):
            board.push_san(move)
            evaluation = minimax(board, depth - 1, alpha, beta, True)[0]
            board.pop()
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            if minEval == evaluation:
                best_move = move
            
        return minEval, best_move

def game():
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not isWin(board):
        print(board)

        print(("White" if board.turn else "Black") + " to play.")
        
        board.push_san(minimax(board, 8, float("-inf"), float("inf"), board.turn)[1])

        moves.append(str(board.peek()))

    #post-game
    print(board)
    if isWin(board) == "White":
        print("White wins")
    elif isWin(board) == "Black":
        print("Black wins")
    print(moves)

game()