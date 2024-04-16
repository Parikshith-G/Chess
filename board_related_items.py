import imports
board = [
    ["BR", "BN", "BB", "WQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BQ", "BP", "BP", "BP", "BP", "BP"],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
]
board_next = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    [".",  ".",  ".",  ".",  ".",  ".",  ".",  "."],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
]


piece_mappings = {
    "BR": imports.BLACK_ROOK_IMAGE,
    "BN": imports.BLACK_KNIGHT_IMAGE,
    "BB": imports.BLACK_BISHOP_IMAGE,
    "BQ": imports.BLACK_QUEEN_IMAGE,
    "BK": imports.BLACK_KING_IMAGE,
    "BP": imports.BLACK_PAWN_IMAGE,
    "WR": imports.WHITE_ROOK_IMAGE,
    "WN": imports.WHITE_KNIGHT_IMAGE,
    "WB": imports.WHITE_BISHOP_IMAGE,
    "WQ": imports.WHITE_QUEEN_IMAGE,
    "WK": imports.WHITE_KING_IMAGE,
    "WP": imports.WHITE_PAWN_IMAGE
}

board_blueprint = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

]

board_checked = [
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
]
