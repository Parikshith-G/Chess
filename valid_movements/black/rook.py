from ..movements.rook import is_valid_rook_move


def is_valid_black_rook_move(current_pos,new_pos,board):
    return is_valid_rook_move(current_pos,new_pos,"W",board)
    