from .bishop import is_valid_bishop_move
from .rook import is_valid_rook_move


def is_valid_queen_move(current_pos,new_pos,opp_col):
    return is_valid_rook_move(current_pos,new_pos,opp_col) or is_valid_bishop_move(current_pos,new_pos,opp_col)