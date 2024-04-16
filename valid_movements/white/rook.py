import imports
from ..movements.rook import is_valid_rook_move
def is_valid_white_rook_move(current_pos,new_pos):
    return is_valid_rook_move(current_pos,new_pos,"B")
    