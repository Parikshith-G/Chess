from .pos_to_coords import coords
import imports
def king_beam_master(pos,col,board):
    x,y=coords(pos)
    
    valid_movements=[
        [-1,-1],[-1,0],[-1,1],
        [0,-1],[0,1],
        [1,-1],[1,0],[1,1]
        ]
    for move in valid_movements:
        dx,dy=move
        new_x,new_y=x+dx,y+dy
        if 0<=new_x<8 and 0<=new_y<8:
            if col=="B":
                board[new_x][new_y][0]=1
            else:
                board[new_x][new_y][1]=1
    return board
                