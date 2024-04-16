def board_to_screen_coords(position,size):
    col = ord(position[0]) - ord('a')
    row = 8 - int(position[1])
    return (col * size, row * size)
