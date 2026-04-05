"""
AI engine using minimax with alpha-beta pruning.
Depth 2 = fast, Depth 3 = medium, Depth 4 = slow but stronger.
"""
import copy
import random
from game_logic import (get_all_legal_moves, move_piece_on_board,
                        is_check_on_board, is_checkmate, is_stalemate)

PIECE_VALUES = {
    'P': 100, 'N': 320, 'B': 330, 'R': 500, 'Q': 900, 'K': 20000
}

PAWN_TABLE = [
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [ 5,  5, 10, 25, 25, 10,  5,  5],
    [ 0,  0,  0, 20, 20,  0,  0,  0],
    [ 5, -5,-10,  0,  0,-10, -5,  5],
    [ 5, 10, 10,-20,-20, 10, 10,  5],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
]
KNIGHT_TABLE = [
    [-50,-40,-30,-30,-30,-30,-40,-50],
    [-40,-20,  0,  0,  0,  0,-20,-40],
    [-30,  0, 10, 15, 15, 10,  0,-30],
    [-30,  5, 15, 20, 20, 15,  5,-30],
    [-30,  0, 15, 20, 20, 15,  0,-30],
    [-30,  5, 10, 15, 15, 10,  5,-30],
    [-40,-20,  0,  5,  5,  0,-20,-40],
    [-50,-40,-30,-30,-30,-30,-40,-50],
]
BISHOP_TABLE = [
    [-20,-10,-10,-10,-10,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5, 10, 10,  5,  0,-10],
    [-10,  5,  5, 10, 10,  5,  5,-10],
    [-10,  0, 10, 10, 10, 10,  0,-10],
    [-10, 10, 10, 10, 10, 10, 10,-10],
    [-10,  5,  0,  0,  0,  0,  5,-10],
    [-20,-10,-10,-10,-10,-10,-10,-20],
]
ROOK_TABLE = [
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 5, 10, 10, 10, 10, 10, 10,  5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [ 0,  0,  0,  5,  5,  0,  0,  0],
]
QUEEN_TABLE = [
    [-20,-10,-10, -5, -5,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5,  5,  5,  5,  0,-10],
    [ -5,  0,  5,  5,  5,  5,  0, -5],
    [  0,  0,  5,  5,  5,  5,  0, -5],
    [-10,  5,  5,  5,  5,  5,  0,-10],
    [-10,  0,  5,  0,  0,  0,  0,-10],
    [-20,-10,-10, -5, -5,-10,-10,-20],
]
KING_TABLE = [
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-20,-30,-30,-40,-40,-30,-30,-20],
    [-10,-20,-20,-20,-20,-20,-20,-10],
    [ 20, 20,  0,  0,  0,  0, 20, 20],
    [ 20, 30, 10,  0,  0, 10, 30, 20],
]
TABLES = {'P': PAWN_TABLE, 'N': KNIGHT_TABLE, 'B': BISHOP_TABLE,
          'R': ROOK_TABLE, 'Q': QUEEN_TABLE, 'K': KING_TABLE}


def evaluate_board(board):
    score = 0
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == '.':
                continue
            color, ptype = piece[0], piece[1]
            val = PIECE_VALUES.get(ptype, 0)
            table = TABLES.get(ptype)
            pos_bonus = (table[r][c] if color == 'W' else table[7 - r][c]) if table else 0
            score += (val + pos_bonus) if color == 'W' else -(val + pos_bonus)
    return score


def minimax(board, depth, alpha, beta, maximizing):
    color = 'W' if maximizing else 'B'

    if depth == 0:
        return evaluate_board(board), None

    moves = get_all_legal_moves(color, board)
    if not moves:
        if is_check_on_board(color, board):
            return (float('-inf') if maximizing else float('inf')), None
        return 0, None  # stalemate

    random.shuffle(moves)
    best_move = None

    if maximizing:
        best = float('-inf')
        for piece, frm, to in moves:
            sim = move_piece_on_board(piece, frm, to, board)
            score, _ = minimax(sim, depth - 1, alpha, beta, False)
            if score > best:
                best, best_move = score, (piece, frm, to)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best, best_move
    else:
        best = float('inf')
        for piece, frm, to in moves:
            sim = move_piece_on_board(piece, frm, to, board)
            score, _ = minimax(sim, depth - 1, alpha, beta, True)
            if score < best:
                best, best_move = score, (piece, frm, to)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best, best_move


def get_best_move(board, ai_color, depth=3):
    maximizing = (ai_color == 'W')
    _, move = minimax(board, depth, float('-inf'), float('inf'), maximizing)
    return move
