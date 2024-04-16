import imports
from .pos_to_coords import coords
from .rook_bishop_beam_validator import helper
def bishop_beam_master(pos,col,board):

    x,y=coords(pos)
    i,j=x,y
    while i>=0 and j>=0:
        check=helper(i,j,x,y,col,board)
        if not check[0]:
            break
        else:
            board=check[1]
        i-=1
        j-=1
    i,j=x,y
    while i<8 and j<8:
        check=helper(i,j,x,y,col,board)
        if not check[0] :
            break
        else:
            board=check[1]
        i+=1
        j+=1
    i,j=x,y
    while i>=0 and j<8:
        check=helper(i,j,x,y,col,board)
        if not check[0] :
            break
        else:
            board=check[1]
        i-=1
        j+=1
    i,j=x,y
    while i<8 and j>=0:
        check=helper(i,j,x,y,col,board)
        if not check[0] :
            break
        else:
            board=check[1]
        i+=1
        j-=1
    return board
            
        
    