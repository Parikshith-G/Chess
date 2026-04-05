"""
Board-agnostic wrappers for move validation and game state checks.
The existing validators use imports.board (global), so we temporarily
swap the global board, call the validator, then restore it.
"""
import copy
import imports
from beams.initializer import initiliazer_main
from is_king_checked.is_check import is_there_a_check


def is_valid_move_on_board(piece, from_pos, to_pos, board):
    """Validate a move against an arbitrary board state."""
    saved = imports.board
    imports.board = board
    result = imports.is_valid_move(piece, from_pos, to_pos)
    imports.board = saved
    return result


def move_piece_on_board(piece, from_pos, to_pos, board, update_ep=True, update_castling=True):
    """Apply a move to a board copy and return it. Also updates imports.en_passant_target."""
    b = copy.deepcopy(board)
    old_x = abs(int(from_pos[1]) - 8)
    old_y = abs(int(ord(from_pos[0]) - ord('a')))
    new_x = abs(int(to_pos[1]) - 8)
    new_y = abs(int(ord(to_pos[0]) - ord('a')))
    b[old_x][old_y] = '.'
    b[new_x][new_y] = piece

    new_ep = None

    if piece == 'WP':
        if old_x - new_x == 2:
            new_ep = imports.board_blueprint[old_x - 1][old_y]
        elif to_pos == imports.en_passant_target and old_y != new_y:
            b[new_x + 1][new_y] = '.'
        elif new_x == 0:
            b[new_x][new_y] = 'WQ'

    elif piece == 'BP':
        if new_x - old_x == 2:
            new_ep = imports.board_blueprint[old_x + 1][old_y]
        elif to_pos == imports.en_passant_target and old_y != new_y:
            b[new_x - 1][new_y] = '.'
        elif new_x == 7:
            b[new_x][new_y] = 'BQ'

    # castling — move the rook too
    elif piece == 'WK':
        if from_pos == 'e1' and to_pos == 'g1':   # white kingside
            b[7][7] = '.'; b[7][5] = 'WR'
        elif from_pos == 'e1' and to_pos == 'c1':  # white queenside
            b[7][0] = '.'; b[7][3] = 'WR'

    elif piece == 'BK':
        if from_pos == 'e8' and to_pos == 'g8':   # black kingside
            b[0][7] = '.'; b[0][5] = 'BR'
        elif from_pos == 'e8' and to_pos == 'c8':  # black queenside
            b[0][0] = '.'; b[0][3] = 'BR'

    if update_ep:
        imports.en_passant_target = new_ep

    if update_castling:
        cr = list(imports.castling_rights)
        if piece == 'WK' or from_pos == 'e1':  cr[0] = cr[1] = False
        if piece == 'WR' and from_pos == 'h1': cr[0] = False
        if piece == 'WR' and from_pos == 'a1': cr[1] = False
        if piece == 'BK' or from_pos == 'e8':  cr[2] = cr[3] = False
        if piece == 'BR' and from_pos == 'h8': cr[2] = False
        if piece == 'BR' and from_pos == 'a8': cr[3] = False
        # also revoke if a rook is captured
        if to_pos == 'h1': cr[0] = False
        if to_pos == 'a1': cr[1] = False
        if to_pos == 'h8': cr[2] = False
        if to_pos == 'a8': cr[3] = False
        imports.castling_rights = cr

    return b


def is_check_on_board(color, board):
    saved = imports.board
    imports.board = board
    checked = initiliazer_main(board, imports.board_blueprint)
    result = is_there_a_check(color, board, checked)
    imports.board = saved
    return result


def get_all_legal_moves(color, board):
    """Return list of (piece, from_pos, to_pos) for all legal moves."""
    moves = []
    saved_ep = imports.en_passant_target
    saved_cr = list(imports.castling_rights)
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == '.' or piece[0] != color:
                continue
            from_pos = imports.board_blueprint[r][c]
            for tr in range(8):
                for tc in range(8):
                    to_pos = imports.board_blueprint[tr][tc]
                    if from_pos == to_pos:
                        continue
                    imports.en_passant_target = saved_ep
                    imports.castling_rights = list(saved_cr)
                    if is_valid_move_on_board(piece, from_pos, to_pos, board):
                        sim = move_piece_on_board(piece, from_pos, to_pos, board,
                                                  update_ep=False, update_castling=False)
                        if not is_check_on_board(color, sim):
                            moves.append((piece, from_pos, to_pos))
    imports.en_passant_target = saved_ep
    imports.castling_rights = list(saved_cr)
    return moves


def is_checkmate(color, board):
    if not is_check_on_board(color, board):
        return False
    return len(get_all_legal_moves(color, board)) == 0


def is_stalemate(color, board):
    if is_check_on_board(color, board):
        return False
    return len(get_all_legal_moves(color, board)) == 0
