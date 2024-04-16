import imports

def print_board():
    t=[]
    for i in imports.board:
        ta=[]
        for j in i:
            if j==".":
                ta.append("  ")
            else:
                ta.append(j)
        t.append(ta)
    for i in t:
        print(i)
    print("\n================================")
def move_piece(piece,current_pos,new_pos,board):
    # print_board()
    old_x=abs(int(current_pos[1])-8)
    old_y=abs(int(ord(current_pos[0])-ord('a')))
    new_x=abs(int(new_pos[1])-8)
    new_y=abs(int(ord(new_pos[0])-ord('a')))
    board[old_x][old_y]="."
    board[new_x][new_y]=piece
    return board
    