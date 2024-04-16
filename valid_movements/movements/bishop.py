import imports

def beam(x,y):
    s=set()
    i,j=x,y
    while i>=0 and j>=0:
        s.add((i,j))
        i-=1
        j-=1
    i,j=x,y
    while i<=7 and j<=7:
        s.add((i,j))
        i+=1
        j+=1
    i,j=x,y
    while i<=7 and j>=0:
        s.add((i,j))
        i+=1
        j-=1
    i,j=x,y
    while i>=0 and j<=7:
        s.add((i,j))
        i-=1
        j+=1
    return s
def is_valid_bishop_move(current_pos,new_pos,opp_col):
    old_x,old_y,new_x,new_y=imports.get_all_coords(current_pos,new_pos)
    if old_x==new_x and old_y==new_y:
        return False
    all_available_moves=beam(old_x,old_y)
    if (new_x,new_y) in all_available_moves:
        flag=True
        if old_x<new_x and old_y<new_y:
            i,j=old_x,old_y
            pos=imports.board_blueprint[i][j]
            piece=imports.get_piece_at_clicked_pos(pos,imports.board)
            while i<=new_x and j<=new_y:
                pos=imports.board_blueprint[i][j]
                piece=imports.get_piece_at_clicked_pos(pos,imports.board)
                if piece:
                    if flag:
                        flag=False
                    else:
                        if (i,j)==(new_x,new_y) and piece[0]==opp_col:
                            return True
                        
                        else:
                            return False
                i+=1
                j+=1
            if not piece:
                return True
            else:
                return False
        elif old_x <new_x and old_y >new_y:
            i,j=old_x,old_y
            pos=imports.board_blueprint[i][j]
            piece=imports.get_piece_at_clicked_pos(pos,imports.board)
            while i<=new_x and j>=new_y:
                pos=imports.board_blueprint[i][j]
                piece=imports.get_piece_at_clicked_pos(pos,imports.board)
                if piece:
                    if flag:
                        flag=False
                    else:
                        if (i,j)==(new_x,new_y) and piece[0]==opp_col:
                            return True
                        else:
                            return False
                i+=1
                j-=1
            if not piece:
                return True
            return False
        elif old_x>new_x and old_y<new_y:
            i,j=old_x,old_y
            pos=imports.board_blueprint[i][j]
            piece=imports.get_piece_at_clicked_pos(pos,imports.board)
            while i>=new_x and j<=new_y:
                pos=imports.board_blueprint[i][j]
                piece=imports.get_piece_at_clicked_pos(pos,imports.board)
                if piece:
                    if flag:
                        flag=False
                    else:
                        if (i,j)==(new_x,new_y) and piece[0]==opp_col:
                            return True
                        else:
                            return False
                i-=1
                j+=1
            if not piece:
                return True
            else:
                return False
        elif old_x>new_x and old_y>new_y:
            i,j=old_x,old_y
            pos=imports.board_blueprint[i][j]
            piece=imports.get_piece_at_clicked_pos(pos,imports.board)
            while i>=new_x and j>=new_y:
                pos=imports.board_blueprint[i][j]
                piece=imports.get_piece_at_clicked_pos(pos,imports.board)
                if piece:
                    if flag:
                        flag=False
                    else:
                        if (i,j)==(new_x,new_y) and piece[0]==opp_col:
                            return True
                        else:
                            return False
                i-=1
                j-=1
            if not piece:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
