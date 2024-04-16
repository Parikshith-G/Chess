import imports 
def is_valid_move(selected_piece,current_pos,new_pos):
    if selected_piece=="BR":
        return imports.is_valid_black_rook_move(current_pos,new_pos)
    elif selected_piece=="BN":
        return imports.is_valid_black_knight_move(current_pos,new_pos)
    elif selected_piece=="BB":
        return imports.is_valid_black_bishop_move(current_pos,new_pos)
    elif selected_piece=="BQ":
        return imports.is_valid_black_queen_move(current_pos,new_pos)
    elif selected_piece=="BK":
        return imports.is_valid_black_king_move(current_pos,new_pos)
    elif selected_piece=="BP":
        return imports.is_valid_black_pawn_move(current_pos,new_pos)
        
    elif selected_piece=="WR":
        return imports.is_valid_white_rook_move(current_pos,new_pos)
    elif selected_piece=="WN":
        return imports.is_valid_white_knight_move(current_pos,new_pos)
    elif selected_piece=="WB":
        return imports.is_valid_white_bishop_move(current_pos,new_pos)
    elif selected_piece=="WQ":
        return imports.is_valid_white_queen_move(current_pos,new_pos)
    elif selected_piece=="WK":
        return imports.is_valid_white_king_move(current_pos,new_pos)
    elif selected_piece=="WP":
        return imports.is_valid_white_pawn_move(current_pos,new_pos)
    print(imports.board)