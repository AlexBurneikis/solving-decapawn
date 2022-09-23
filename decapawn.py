import chess

#function to determine wether anyone has won
def isWin(board):
    #check if a pawn has reached the opposite rank
    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}1')
        
        if board.piece_at(square) == None: continue
        
        if board.piece_at(square).color == chess.BLACK:
            winner = "Black"
            print(winner + " wins")
            return True
     
    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}5')
        
        if board.piece_at(square) == None: continue
        
        if board.piece_at(square).color == chess.WHITE:
            winner = "White"
            print(winner + " wins")
            return True

    if board.is_stalemate():
        if board.turn:
            winner = "Black"
        else:
            winner = "White"
            
        print("Stalemate")
        print(winner + " wins")
        return True
    
    return False

def getMove(board):
    move = input(("White " if board.turn else "Black ") + "move: ")
    try:
        board.parse_san(move)
    except ValueError:
        print("Invalid move")
        getMove(board)
        return
        
    legalMoves = [str(i) for i in board.legal_moves]
        
    toRemove = []
    for i in legalMoves:
        if (int(i[3]) - int(i[1])) == 2:
            toRemove.append(i)
        
    for i in toRemove:
        legalMoves.remove(i)
    
    if str(board.parse_san(move)) in legalMoves:
        board.push_san(move)
    else:
        print("Invalid move")
        getMove(board)

def game():
    #make decapawn game
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")
    
    while not isWin(board):
        print(board)
        getMove(board)
        
game()
