import imports
from .pos_to_coords import coords
def knight_beam_master(pos,col,board):
    
    x,y=coords(pos)
    
    
    moves=[[-1,-2],[1,-2],[-2,-1],[2,-1],[-2,1],[2,1],[-1,2],[1,2]]
    for move in moves:
        dy,dx=move
        new_x,new_y=dx+x,dy+y
        if 0<=new_x<8 and 0<=new_y<8:
            if col=="B":
                board[new_x][new_y][0]=1
            else:
                board[new_x][new_y][1]=1
    return board
                