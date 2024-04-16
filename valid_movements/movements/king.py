import imports
def validate_move(x,y,col):
    pos=imports.board_blueprint[x][y]
    piece=imports.get_piece_at_clicked_pos(pos,imports.board)
    if not piece:
        return True
    if piece and piece[0]==col:
        return True
    return False
def is_valid_king_move(current_pos,new_pos,col):
    old_x,old_y,new_x,new_y=imports.get_all_coords(current_pos,new_pos)
    valid_movements=[
    [-1,-1],[-1,0],[-1,1],
    [0,-1],[0,1],
    [1,-1],[1,0],[1,1]
    ]
    for move in valid_movements:
        dx,dy=move
        mod_x,mod_y=old_x+dx,old_y+dy
        if (0<=mod_x<=8 and 0<=mod_y<=8) and (mod_x==new_x and mod_y==new_y):
            return validate_move(new_x,new_y,col)
    return False
        
    