import imports
def is_valid_white_pawn_move(current_pos, new_pos):
    old_x, old_y, new_x, new_y = imports.get_all_coords(current_pos, new_pos)
    if old_x < new_x:
        return False
    # one square forward
    if old_x - 1 == new_x and old_y == new_y:
        return imports.get_piece_at_clicked_pos(new_pos, imports.board) is None
    # two squares forward from starting rank (row index 6)
    if old_x == 6 and new_x == 4 and old_y == new_y:
        mid = imports.board_blueprint[old_x - 1][old_y]
        return (imports.get_piece_at_clicked_pos(mid, imports.board) is None and
                imports.get_piece_at_clicked_pos(new_pos, imports.board) is None)
    # diagonal — real capture or en passant
    if old_x - 1 == new_x and abs(old_y - new_y) == 1:
        target = imports.get_piece_at_clicked_pos(new_pos, imports.board)
        if target and target[0] == "B":
            return True
        if new_pos == imports.en_passant_target:
            return True
    return False
