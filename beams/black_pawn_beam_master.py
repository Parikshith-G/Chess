import imports
from .pos_to_coords import coords
def black_pawn_beam_master(pos,board):
    x,y=coords(pos)
    movements=[[1,-1],[1,1]]
    for move in movements:
        dx,dy=move
        new_x,new_y=x+dx,y+dy
        if 0<=new_x<8 and 0<=new_y<8:
            board[new_x][new_y][0]=1
    return board