from ..movements.knight import is_valid_knight_move

def is_valid_black_knight_move(current_pos,new_pos):
    return is_valid_knight_move(current_pos,new_pos,"W")