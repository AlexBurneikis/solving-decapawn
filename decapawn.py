import chess

#create a board
board = chess.Board()

#clear the board
board.clear_board()

#put white pawns on a1, b1, c1, d1, e1 and black pawns on a5, b5, c5, d5, e5
#make an array of these positions
#use a for loop to iterate through the array and place the pawns

wPawnStartPositions = ["a1", "b1", "c1", "d1", "e1"]
bPawnStartPositions = ["a5", "b5", "c5", "d5", "e5"]

for i in wPawnStartPositions:
    board.set_piece_at(chess.parse_square(i), chess.Piece(chess.PAWN, chess.WHITE))

for i in bPawnStartPositions:
    board.set_piece_at(chess.parse_square(i), chess.Piece(chess.PAWN, chess.BLACK))

#show the board
print(board)

def didLose():
    #check if it is stalemate
    if board.is_stalemate():
        print("Stalemate")
        return True

def checkWin(whiteTurn):
    #check if a pawn has reached the other side

    possibleFiles = ["a", "b", "c", "d", "e"]

    if whiteTurn:
        #check the fifth rank for white pawns
        for i in possibleFiles:
            if board.piece_at(chess.parse_square(i + "5")) != None:
                if board.piece_at(chess.parse_square(i + "5")).color == chess.WHITE:
                    print("White wins")
                    gameRunning = False
                    return True
    else:
        #check the first rank for black pawns
        for i in possibleFiles:
            if board.piece_at(chess.parse_square(i + "1")) != None:
                if board.piece_at(chess.parse_square(i + "1")).color == chess.BLACK:
                    print("Black wins")
                    gameRunning = False
                    return True

def getMove():
    #get the move from the user
    #check if the move is valid
    #if the move is valid, make the move
    #if the move is not valid, ask for a new move

    move = input("Enter your move: ")

    #test if the move gives ValueError
    try:
        board.parse_san(move)
    except ValueError:
        print("Invalid move")
        getMove()
        return

    legalMoves = board.legal_moves
    legalMoves = [str(i) for i in legalMoves]
    
    toRemove = []
    for i in legalMoves:
        if (int(i[3]) - int(i[1])) == 2:
            toRemove.append(i)

    #remove toRemove from legalMoves
    for i in toRemove:
        legalMoves.remove(i)

    #if legalMoves has the move, make the move
    if str(board.parse_san(move)) in legalMoves:
        board.push_san(move)
    else:
        print("Invalid move")
        getMove()

def start():
    #if a pawn reaches the other side you win
    #if you cannot move you lose

    isWhiteTurn = True
    gameRunning = True

    while gameRunning:
        if didLose():
            print("White wins" if isWhiteTurn else "Black wins")
            gameRunning = False
            continue

        getMove()

        print(board)

        checkWin(isWhiteTurn)

start()