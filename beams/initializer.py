import imports
from beams.rook_beam_master import rook_beam_master
from beams.bishop_beam_master import bishop_beam_master
from beams.black_pawn_beam_master import black_pawn_beam_master
from beams.king_beam_master import king_beam_master
from beams.knight_beam_master import knight_beam_master
from beams.queen_beam_master import queen_beam_master
from beams.white_pawn_beam_master import white_pawn_beam_master
from beams.new_checked_board import new_checked_board
from beams.reset_board import reset_board


d={
    "BR":"BR",
    "BN":"BN",
    "BB":"BB",
    "BQ":"BQ",
    "BK":"BK",
    "BP":"BP",
    "WR":"WR",
    "WN":"WN",
    "WB":"WB",
    "WQ":"WQ",
    "WK":"WK",
    "WP":"WP",
}
def initiliazer_main(board,board_blueprint):
    board_init=[[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
]
    for i in range(len(board)):
        for j in range(len(board[i])):
            piece=board[i][j]
            if piece in d:
                piece_type, pos = piece, board_blueprint[i][j]
                if piece_type == "BR":
                    board_init= rook_beam_master(pos, "B",board_init)
                elif piece_type == "BN":
                    board_init= knight_beam_master(pos, "B",board_init)
                elif piece_type == "BB":
                    board_init= bishop_beam_master(pos, "B",board_init)
                elif piece_type == "BQ":
                    board_init= queen_beam_master(pos, "B",board_init)
                elif piece_type == "BK":
                    board_init= king_beam_master(pos, "B",board_init)
                elif piece_type == "BP":
                    board_init= black_pawn_beam_master(pos,board_init)
                elif piece_type == "WR":
                    board_init= rook_beam_master(pos, "W",board_init)
                elif piece_type == "WN":
                    board_init= knight_beam_master(pos, "W",board_init)
                elif piece_type == "WB":
                    board_init= bishop_beam_master(pos, "W",board_init)
                elif piece_type == "WQ":
                    board_init= queen_beam_master(pos, "W",board_init)
                elif piece_type == "WK":
                    board_init= king_beam_master(pos, "W",board_init)
                elif piece_type == "WP":
                    board_init= white_pawn_beam_master(pos,board_init)
    return board_init
