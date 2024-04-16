import imports
from beams.initializer import initiliazer_main
import copy

imports.pygame.init()
screen = imports.pygame.display.set_mode(
    (imports.SCREEN_WIDTH, imports.SCREEN_HEIGHT))

running = True
current_player = 'W'
is_player_checked = False
while running:
    for event in imports.pygame.event.get():
        if event.type == imports.pygame.QUIT:
            running = False

        elif event.type == imports.pygame.MOUSEBUTTONDOWN and event.button == 1:
            for b in (imports.board):
                print(b)
            mouse_pos = imports.pygame.mouse.get_pos()
            clicked_pos = imports.mouse_to_board_coordinates(
                mouse_pos, imports.SQUARE_SIZE)
            piece_at_clicked_pos = imports.get_piece_at_clicked_pos(
                clicked_pos, imports.board)
            if piece_at_clicked_pos:
                selected_piece = piece_at_clicked_pos
                selected_piece_pos = clicked_pos
            else:
                selected_piece = None
                selected_piece_pos = None
        elif event.type == imports.pygame.MOUSEBUTTONUP and event.button == 1:
            imports.board_checked = initiliazer_main(
                imports.board, imports.board_blueprint)
            if selected_piece and current_player == selected_piece[0]:
                new_pos = imports.mouse_to_board_coordinates(
                    imports.pygame.mouse.get_pos(), imports.SQUARE_SIZE)
                if imports.is_valid_move(selected_piece, selected_piece_pos, new_pos):
                    imports.board_checked = initiliazer_main(
                        imports.board, imports.board_blueprint)
                    board_simulation = copy.deepcopy(imports.board)
                    board_simulation = imports.move_piece(
                        selected_piece, selected_piece_pos, new_pos, board_simulation)
                    board_checked_simulation = copy.deepcopy(
                        initiliazer_main(board_simulation, imports.board_blueprint))
                    if imports.is_there_a_check(current_player, board_simulation, board_checked_simulation):

                        if imports.is_there_a_check(current_player, board_simulation, board_checked_simulation):
                            selected_piece = None

                            selected_piece_pos = None
                        else:

                            imports.board = board_simulation
                    else:
                        print(current_player)
                        imports.board = imports.move_piece(
                            selected_piece, selected_piece_pos, new_pos, imports.board)
                        imports.board_checked = initiliazer_main(
                            imports.board, imports.board_blueprint)
                        current_player = "B" if current_player == "W" else "W"
                selected_piece = None
                selected_piece_pos = None

    screen.fill(imports.WHITE)
    for r in range(8):
        for c in range(8):
            color = imports.WHITE if (r + c) % 2 == 0 else imports.BLACK
            imports.pygame.draw.rect(screen, color, (c * imports.SQUARE_SIZE,
                                     r * imports.SQUARE_SIZE, imports.SQUARE_SIZE, imports.SQUARE_SIZE))
            letter = chr(ord('a') + c)
            number = str(8 - r)
            coordinate = letter + number
            font = imports.pygame.font.Font(None, 20)
            text = font.render(coordinate, True, (0, 0, 0))
            text_rect = text.get_rect(
                center=((c + 0.9) * imports.SQUARE_SIZE-5, (r) * imports.SQUARE_SIZE+4.8))
            screen.blit(text, text_rect)
    for i in range(imports.BOARD_SIZE):
        for j in range(imports.BOARD_SIZE):
            piece = imports.board[i][j]
            if piece in imports.piece_mappings:
                piece_name = imports.piece_mappings[piece]
                piece_pos = imports.board_blueprint[i][j]
                screen.blit(piece_name, imports.board_to_screen_coords(
                    piece_pos, imports.SQUARE_SIZE))

    imports.pygame.display.flip()


imports.pygame.quit()
imports.sys.exit()
