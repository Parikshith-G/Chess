def mouse_to_board_coordinates(position,size):
    x_coord,y_coord=position[1]//size,position[0]//size
    return chr(ord('a')+y_coord)+str(8-x_coord)
