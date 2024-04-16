from ..movements.king import is_valid_king_move

def is_valid_white_king_move(current_pos,new_pos):
    return is_valid_king_move(current_pos,new_pos,"B")