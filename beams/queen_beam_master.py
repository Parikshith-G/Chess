import imports
from .bishop_beam_master import bishop_beam_master
from .rook_beam_master import rook_beam_master

def queen_beam_master(pos,col,board):
    
    board=rook_beam_master(pos,col,board)
    board=bishop_beam_master(pos,col,board)
    return board
    