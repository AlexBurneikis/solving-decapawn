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

    return legalMoves

def canWin(board, player):
    #check if player can win on next move
    legalMoves = generateLegalMoves(board)

    for i in legalMoves:
        board.push_san(i)
        if isWin(board) == player:
            return True
        board.pop()

    return False

def getAiMove(board):
    legalMoves = generateLegalMoves(board)

    player = "White" if board.turn else "Black"
    opponent = "Black" if board.turn else "White"
    
    #randomize legalMoves
    random.shuffle(legalMoves)

    #simulate all moves
    for i in legalMoves:
        board.push_san(i)
        if isWin(board) == player:
            return

        
        #check if opponent can win on the next move
        if canWin(board, opponent):
            board.pop()
            continue



    #if no winning moves, make random move
    print(player + " gave up")   
    board.push_san(legalMoves[0])
    return

def game():
    # make decapawn game
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not isWin(board):
        print(board)
        getAiMove(board)

        moves.append(str(board.peek()))

    print(board)
    if isWin(board) == "White":
        print("White wins")
    elif isWin(board) == "Black":
        print("Black wins")

    print(moves)

game()