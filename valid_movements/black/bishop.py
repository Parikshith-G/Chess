from ..movements.bishop import is_valid_bishop_move
def is_valid_black_bishop_move(current_pos,new_pos):
    return is_valid_bishop_move(current_pos,new_pos,"W")