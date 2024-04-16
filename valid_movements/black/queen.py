from ..movements.queen import is_valid_queen_move
def is_valid_black_queen_move(current_pos,new_pos):
    
    return is_valid_queen_move(current_pos,new_pos,"W")