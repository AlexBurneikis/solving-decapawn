import chess
import chess.pgn
from get_move import get_move
from decapawn_moves import get_decapawn_moves
from decapawn_win import is_win

def get_player_move(board):
    while True:
        try:
            move = board.parse_san(input("Enter move: "))
            if move in get_decapawn_moves(board):
                return move   
        except:
            pass

def game(depth):
    board = chess.Board()
    board.set_board_fen("8/8/8/ppppp3/8/8/8/PPPPP3")

    moves = []

    while not is_win(board):
        print(board)

        move = get_move(board, depth) #if board.turn else get_player_move(board)

        print(str(move))
        board.push(move)
        moves.append(str(move))

    print(board)
    print(moves)

if __name__ == "__main__":
    game(6)