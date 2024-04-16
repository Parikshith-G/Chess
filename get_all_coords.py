def get_all_coords(current_pos,new_pos):
    old_x=abs(int(current_pos[1])-8)
    old_y=abs(int(ord(current_pos[0])-ord('a')))
    new_x=abs(int(new_pos[1])-8)
    new_y=abs(int(ord(new_pos[0])-ord('a')))
    return old_x,old_y,new_x,new_y
    