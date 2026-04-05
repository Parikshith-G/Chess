import imports
from is_king_checked.is_check import is_there_a_check
from beams.initializer import initiliazer_main

def validate_move(x, y, col):
    pos = imports.board_blueprint[x][y]
    piece = imports.get_piece_at_clicked_pos(pos, imports.board)
    if not piece:
        return True
    if piece and piece[0] == col:
        return True
    return False

def squares_safe(color, squares, board):
    """Return True if none of the given squares are attacked by the opponent."""
    checked = initiliazer_main(board, imports.board_blueprint)
    # beam stores [black_attacks, white_attacks]
    # to protect white king, check black isn't attacking (idx 0)
    # to protect black king, check white isn't attacking (idx 1)
    idx = 0 if color == "W" else 1
    for sq in squares:
        c = ord(sq[0]) - ord('a')
        r = 8 - int(sq[1])
        if checked[r][c][idx] == 1:
            return False
    return True

def is_valid_king_move(current_pos, new_pos, col):
    old_x, old_y, new_x, new_y = imports.get_all_coords(current_pos, new_pos)
    color = "W" if col == "B" else "B"   # col is opponent color; color is the moving king's color

    # normal one-square moves
    valid_movements = [
        [-1,-1],[-1,0],[-1,1],
        [0,-1],[0,1],
        [1,-1],[1,0],[1,1]
    ]
    for dx, dy in valid_movements:
        mod_x, mod_y = old_x + dx, old_y + dy
        if (0 <= mod_x < 8 and 0 <= mod_y < 8) and (mod_x == new_x and mod_y == new_y):
            return validate_move(new_x, new_y, col)

    # castling
    cr = imports.castling_rights
    board = imports.board

    if color == "W" and old_x == 7 and old_y == 4:
        # white kingside: king e1→g1, rook h1→f1
        if cr[0] and new_x == 7 and new_y == 6:
            if board[7][5] == '.' and board[7][6] == '.':
                if squares_safe("W", ["e1","f1","g1"], board):
                    return True
        # white queenside: king e1→c1, rook a1→d1
        if cr[1] and new_x == 7 and new_y == 2:
            if board[7][3] == '.' and board[7][2] == '.' and board[7][1] == '.':
                if squares_safe("W", ["e1","d1","c1"], board):
                    return True

    if color == "B" and old_x == 0 and old_y == 4:
        # black kingside: king e8→g8, rook h8→f8
        if cr[2] and new_x == 0 and new_y == 6:
            if board[0][5] == '.' and board[0][6] == '.':
                if squares_safe("B", ["e8","f8","g8"], board):
                    return True
        # black queenside: king e8→c8, rook a8→d8
        if cr[3] and new_x == 0 and new_y == 2:
            if board[0][3] == '.' and board[0][2] == '.' and board[0][1] == '.':
                if squares_safe("B", ["e8","d8","c8"], board):
                    return True

    return False
