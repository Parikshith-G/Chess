def get_piece_at_clicked_pos(clicked_pos,board):
    c=abs(int(ord(clicked_pos[0])-ord('a')))
    r=abs(int(clicked_pos[1])-8)
    piece=board[r][c]
    if piece!=".":
        return piece
    return None

