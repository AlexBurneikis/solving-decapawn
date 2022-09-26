import random
from tabnanny import check
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

def getBestMove(board, depth, color):
    legalMoves = generateLegalMoves(board)

    bestMove = legalMoves[0]
    
    if depth == 0:
        return bestMove

    bestScore = 0

    for i in legalMoves:
        board.push_san(i)
        if isWin(board):
            board.pop()
            return i
        board.push_san(getBestMove(board, depth - 1, ("White" if color == "Black" else "Black")))
        score = evaluate(board)
        board.pop()
        board.pop()

        if score >= bestScore and color == "White":
            bestScore = score
            bestMove = i

        if score <= bestScore and color == "Black":
            bestScore = score
            bestMove = i

    return bestMove

def getAiMove(board):
    legalMoves = generateLegalMoves(board)

    player = "White" if board.turn else "Black"

    #if player can win, win
    for i in legalMoves:
        board.push_san(i)
        if isWin(board) == player:
            board.pop()
            return i
        board.pop()

    return getBestMove(board, 4, player)

def game():
    # make decapawn game
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not isWin(board):
        print(board)
        board.push_san(getAiMove(board))

        moves.append(str(board.peek()))

    print(board)
    if isWin(board) == "White":
        print("White wins")
    elif isWin(board) == "Black":
        print("Black wins")

    print(moves)

game()