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

    return legalMoves

def checkDeeper(board, depth, opponent):
    if depth == 0:
        return isWin(board)
    else:
        legalMoves = generateLegalMoves(board)
        for i in legalMoves:
            board.push_san(i)
            if isWin(board) == opponent:
                    board.pop()
                    continue
            checkDeeper(board, depth - 1, opponent)
            board.pop()
            return

def getAiMove(board):
    legalMoves = generateLegalMoves(board)

    player = "White" if board.turn else "Black"
    opponent = "Black" if board.turn else "White"
    
    #randomize legalMoves
    random.shuffle(legalMoves)

    #simulate all moves
    for i in legalMoves:
        try: 
            board.push_san(i)
        except ValueError:
            continue
        if isWin(board) == player:
            return
        if isWin(board) == opponent:
            board.pop()
            continue
        if isWin(board) != opponent:
            #check if the opponent can win on the next move
            legalMoves = generateLegalMoves(board)

            checkDeeper(board, 1, opponent)

    legalMoves = generateLegalMoves(board)
    board.push_san(legalMoves[0])
    return
        

def game():
    # make decapawn game
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    while not isWin(board):
        print(board)
        getAiMove(board)

    print(board)
    if isWin(board) == "White":
        print("White wins")
    elif isWin(board) == "Black":
        print("Black wins")


game()
