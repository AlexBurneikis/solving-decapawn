def get_decapawn_moves(board):
    legal_moves = [i for i in board.legal_moves]

    remove_moves = []
    for move in legal_moves:
        #if pawn moves forward 2 squares remove it
        start = str(move)[3]
        end = str(move)[1]
        if int(end) - int(start) == 2:
            remove_moves.append(move)

    for move in remove_moves:
        legal_moves.remove(move)

    return legal_moves