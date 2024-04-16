import imports

def is_valid_rook_move(current_pos,new_pos,color):
    old_x,old_y,new_x,new_y=imports.get_all_coords(current_pos,new_pos)
    if old_x==new_x and old_y==new_y:
        return False
    available_x_moves,available_y_moves=[],[]
    for i in range(0,8):
        available_y_moves.append(imports.board_blueprint[old_x][i])
        available_x_moves.append(imports.board_blueprint[i][old_y])
    pieces_in_rows,pieces_in_cols=[],[]
    for i in available_x_moves:
        pieces_in_rows.append(imports.get_piece_at_clicked_pos(i,imports.board))
    for j in available_y_moves:
        pieces_in_cols.append(imports.get_piece_at_clicked_pos(j,imports.board))

    if (old_x==new_x and new_pos in available_y_moves):
        if old_y>new_y:
            for i in range(old_y-1,new_y-1,-1):
                existing_piece=imports.board_blueprint[old_x][i]
                piece_present=True if imports.get_piece_at_clicked_pos(existing_piece,imports.board) else False
                if piece_present:
                    that_piece=imports.get_piece_at_clicked_pos(existing_piece,imports.board)
                    if that_piece ==imports.get_piece_at_clicked_pos(new_pos,imports.board) and imports.board_blueprint[old_x][i]==new_pos:
                        if that_piece[0]==color:
                            return True
                        else:
                            return False
                    else:
                        return False
              
        else:
            for i in range(old_y+1,new_y+1):
                existing_piece=imports.board_blueprint[old_x][i]
                piece_present=True if imports.get_piece_at_clicked_pos(existing_piece,imports.board) else False
                if piece_present:
                    that_piece=imports.get_piece_at_clicked_pos(existing_piece,imports.board)
                    if that_piece ==imports.get_piece_at_clicked_pos(new_pos,imports.board) and imports.board_blueprint[old_x][i]==new_pos:
                        if that_piece[0]==color:
                            return True
                        else:
                            return False
                    else:
                        return False
        
        return True
    elif (old_y==new_y and new_pos in available_x_moves):
        if new_x>old_x:
            for i in range(old_x+1,new_x+1):
                existing_piece=imports.board_blueprint[i][old_y]
                piece_present=True if imports.get_piece_at_clicked_pos(existing_piece,imports.board) else False
                if piece_present:
                    that_piece=imports.get_piece_at_clicked_pos(existing_piece,imports.board)
                    if that_piece ==imports.get_piece_at_clicked_pos(new_pos,imports.board) and imports.board_blueprint[i][old_y]==new_pos:
                        if that_piece[0]==color:
                            return True
                        else:
                            return False
                    else:
                        return False
        else:
            for i in range(old_x-1,new_x-1,-1):
                existing_piece=imports.board_blueprint[i][old_y]
                piece_present=True if imports.get_piece_at_clicked_pos(existing_piece,imports.board) else False
                if piece_present:
                    that_piece=imports.get_piece_at_clicked_pos(existing_piece,imports.board)
                    if that_piece ==imports.get_piece_at_clicked_pos(new_pos,imports.board) and imports.board_blueprint[i][old_y]==new_pos:
                        if that_piece[0]==color:
                            return True
                        else:
                            return False
                    else:
                        return False
        return True
    return False