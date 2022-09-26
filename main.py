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

#def getBestMove(board, depth, color, calculatedBoards, calculatedScores):
    legalMoves = generateLegalMoves(board)

    #guard statement if reach max depth
    if depth == 0: return legalMoves[0]

    #set defaults
    bestMove = legalMoves[0]
    bestScore = 0

    for i in legalMoves:
        board.push_san(i)

        if isWin(board):
            board.pop()
            return i

        lookedDeeper = False
        if board.fen() in calculatedBoards:
            index = calculatedBoards.index(board.fen())
            score = calculatedScores[index]
        else:
            #look deeper
            board.push_san(getBestMove(board, depth - 1, not color, calculatedBoards, calculatedScores))
            score = evaluate(board)
            lookedDeeper = True

        if color:
            if score > bestScore:
                bestScore = score
                bestMove = i
        else:
            if score < bestScore:
                bestScore = score
                bestMove = i

        calculatedBoards.append(board.fen())
        calculatedScores.append(score)

        #go back to previous state
        if lookedDeeper:
            board.pop()
        board.pop()

        #see if this move is better than the previous best move

    return bestMove

def max(score, bestScore):
    if score > bestScore:
        return score
    return bestScore

def min(score, bestScore):
    if score < bestScore:
        return score
    return bestScore

def minimax(board, depth, maxPlayer):
    if depth == 0 or isWin(board):
        return evaluate(board), board

    if maxPlayer:
        maxEval = float('-inf')
        best_move = None
        for move in generateLegalMoves(board):
            board.push_san(move)
            evaluation = minimax(board, depth - 1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            board.pop()
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in generateLegalMoves(board):
            board.push_san(move)
            evaluation = minimax(board, depth - 1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            board.pop()
        return minEval, best_move

def game():
    board = chess.Board()

    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not isWin(board):
        print(board)

        print(("White" if board.turn else "Black") + " to play.")

        #calculatedBoards = []
        #calculatedScores = []
        #board.push_san(getBestMove(board, 7, board.turn, calculatedBoards, calculatedScores))
        
        board.push_san(minimax(board, 7, board.turn)[1])

        moves.append(str(board.peek()))

    #post-game
    print(board)
    if isWin(board) == "White":
        print("White wins")
    elif isWin(board) == "Black":
        print("Black wins")
    print(moves)

game()