import imports
def helper(i,j,x,y,color,board):
    piece=imports.get_piece_at_clicked_pos(imports.board_blueprint[i][j],imports.board)
    if piece:
        if (i,j)==(x,y):
            return [True,board]
        elif (i,j)!=(x,y):
            if color=="B":
                board[i][j][0]=1
            else:
                board[i][j][1]=1
            return [False,board]
        else:
            return [False,board]
    else:
        if color=="B":
            board[i][j][0]=1
        else:
            board[i][j][1]=1
        return [True,board]
        
    