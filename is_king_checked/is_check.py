def is_there_a_check(color,board,board_checked):
    for i in board_checked:
        print(i)
    print('\n\n')
    piece=color+"K"
    for i in range(len(board)):
        for j in range(len(board[i])):
            if piece==board[i][j]:
                idx=1 if color=="B" else 0
                if board_checked[i][j][idx]==1:
                    return True
            
    return False
            
            
        