from .pos_to_coords import coords
import imports
from .rook_bishop_beam_validator import helper


def rook_beam_master(pos,color,board):

    x,y=coords(pos)
    i,j=x,y
    while i>=0:
        check=helper(i,j,x,y,color,board)
        if check[0]==False:
            break
        else:
            board=check[1]
        i-=1
    i,j=x,y
    while i<8:
        check=helper(i,j,x,y,color,board)
        if not check[0]:
            break
        else:
            board=check[1]
        i+=1
    i,j=x,y
    while j<8:
        check=helper(i,j,x,y,color,board)
        if not check[0]:
            break
        else:
            board=check[1]
        j+=1
    i,j=x,y
    while j>=0:
        check=helper(i,j,x,y,color,board)
        if not check[0]:
            break
        else:
            board=check[1]
        j-=1

    
    return board
    

