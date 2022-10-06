import chess

def is_win(board):
    if board.is_game_over():
        return True
        
    #check if pawn has reached opposite rank
    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}1')

        if board.piece_at(square) is None:
            continue

        if board.piece_at(square).color == chess.BLACK:
            return True

    for i in ["a", "b", "c", "d", "e"]:
        square = chess.parse_square(f'{i}5')

        if board.piece_at(square) is None:
            continue

        if board.piece_at(square).color == chess.WHITE:
            return True
    
    return False