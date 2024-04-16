import imports

def is_valid_black_pawn_move(current_pos,new_pos):
    old_x,old_y,new_x,new_y=imports.get_all_coords(current_pos,new_pos)
    if old_x>new_x:
        return False
    elif old_x+1==new_x and old_y==new_y and imports.get_piece_at_clicked_pos(new_pos,imports.board) == None:
        return True
    elif abs(old_y-new_y)==1 and old_x+1==new_x and imports.get_piece_at_clicked_pos(new_pos,imports.board) and imports.get_piece_at_clicked_pos(new_pos,imports.board)[0]=="W":
        return True
    return False

