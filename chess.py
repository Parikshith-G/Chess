import copy
import threading
import imports
from beams.initializer import initiliazer_main
from is_king_checked.is_check import is_there_a_check
from game_logic import (is_valid_move_on_board, move_piece_on_board,
                        is_check_on_board, is_checkmate, is_stalemate,
                        get_all_legal_moves)
from ai import get_best_move
from menu import show_menu, show_game_over

# ── colours ──────────────────────────────────────────────────────────────────
LIGHT_SQ    = (240, 217, 181)
DARK_SQ     = (181, 136,  99)
HIGHLIGHT   = (186, 202,  68, 160)   # selected square
LEGAL_DOT   = (100, 200, 100, 140)   # legal-move dot
CHECK_COL   = (220,  50,  50, 160)   # king-in-check tint
LAST_MOVE   = (100, 200, 100, 140)   # last-move highlight (light green)
PREMOVE_COL = (100, 150, 255, 130)   # premove highlight (blue)
STATUS_BG   = (30,  30,  30)
STATUS_FG   = (255, 255, 255)
AI_THINKING = (255, 200,  50)

AI_DEPTH  = 3
AI_COLOR  = 'B'


def fresh_board():
    return [row[:] for row in imports.board_next]


def sq_to_rc(pos):
    """Algebraic pos → (row, col) screen indices."""
    return 8 - int(pos[1]), ord(pos[0]) - ord('a')


def draw_board(screen, sq, board, selected_pos, legal_moves,
               current_player, last_move, premove):
    font_coord = imports.pygame.font.Font(None, 20)

    for r in range(8):
        for c in range(8):
            color = LIGHT_SQ if (r + c) % 2 == 0 else DARK_SQ
            imports.pygame.draw.rect(screen, color, (c * sq, r * sq, sq, sq))
            lbl = chr(ord('a') + c) + str(8 - r)
            txt = font_coord.render(lbl, True, (80, 80, 80))
            screen.blit(txt, txt.get_rect(
                center=((c + 0.9) * sq - 5, r * sq + 5)))

    def tint(pos, rgba):
        row, col = sq_to_rc(pos)
        s = imports.pygame.Surface((sq, sq), imports.pygame.SRCALPHA)
        s.fill(rgba)
        screen.blit(s, (col * sq, row * sq))

    # last-move highlight (light green)
    if last_move:
        tint(last_move[0], LAST_MOVE)
        tint(last_move[1], LAST_MOVE)

    # premove highlight (blue)
    if premove:
        tint(premove[0], PREMOVE_COL)
        tint(premove[1], PREMOVE_COL)

    # selected square
    if selected_pos:
        tint(selected_pos, HIGHLIGHT)

    # king in check
    for color_c in ('W', 'B'):
        if is_check_on_board(color_c, board):
            for ri in range(8):
                for ci in range(8):
                    if board[ri][ci] == color_c + 'K':
                        tint(imports.board_blueprint[ri][ci], CHECK_COL)

    # legal move dots
    dot_surf = imports.pygame.Surface((sq, sq), imports.pygame.SRCALPHA)
    dot_surf.fill((0, 0, 0, 0))
    imports.pygame.draw.circle(dot_surf, LEGAL_DOT, (sq // 2, sq // 2), sq // 6)
    for _, _, to_pos in legal_moves:
        row, col = sq_to_rc(to_pos)
        screen.blit(dot_surf, (col * sq, row * sq))

    # pieces
    for ri in range(8):
        for ci in range(8):
            piece = board[ri][ci]
            if piece in imports.piece_mappings:
                pos = imports.board_blueprint[ri][ci]
                screen.blit(imports.piece_mappings[piece],
                            imports.board_to_screen_coords(pos, sq))


def draw_status(screen, sq, current_player, mode, ai_thinking, premove):
    bar_h = 40
    bar = imports.pygame.Surface((sq * 8, bar_h))
    bar.fill(STATUS_BG)
    font = imports.pygame.font.Font(None, 34)

    if premove:
        msg = f"Premove queued: {premove[0]}→{premove[1]}  (Right-click to cancel)"
        col = PREMOVE_COL
    elif ai_thinking:
        msg = "Computer is thinking..."
        col = AI_THINKING
    else:
        who = "White" if current_player == 'W' else "Black"
        tag = " (You)" if (mode == 'pvc' and current_player != AI_COLOR) else \
              " (CPU)" if (mode == 'pvc' and current_player == AI_COLOR) else ""
        msg = f"{who}'s turn{tag}"
        col = STATUS_FG

    txt = font.render(msg, True, col)
    bar.blit(txt, txt.get_rect(center=(sq * 4, bar_h // 2)))
    screen.blit(bar, (0, sq * 8))


def show_promotion_menu(screen, sq, color):
    options = ['Q', 'R', 'B', 'N']
    labels  = ['Queen', 'Rook', 'Bishop', 'Knight']
    font = imports.pygame.font.Font(None, 48)
    rects = []
    panel_w, panel_h = 300, 280
    px = sq * 4 - panel_w // 2
    py = sq * 4 - panel_h // 2

    while True:
        mx, my = imports.pygame.mouse.get_pos()
        for event in imports.pygame.event.get():
            if event.type == imports.pygame.QUIT:
                imports.pygame.quit()
                raise SystemExit
            if event.type == imports.pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, r in enumerate(rects):
                    if r.collidepoint(mx, my):
                        return color + options[i]

        overlay = imports.pygame.Surface((sq * 8, sq * 8), imports.pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))
        imports.pygame.draw.rect(screen, (50, 50, 50), (px, py, panel_w, panel_h), border_radius=12)
        title = font.render("Promote to:", True, (255, 215, 0))
        screen.blit(title, title.get_rect(center=(px + panel_w // 2, py + 30)))

        rects = []
        for i, lbl in enumerate(labels):
            r = imports.pygame.Rect(px + 30, py + 70 + i * 50, panel_w - 60, 40)
            rects.append(r)
            hov = r.collidepoint(mx, my)
            imports.pygame.draw.rect(screen, (100, 160, 210) if hov else (70, 130, 180), r, border_radius=8)
            t = font.render(lbl, True, (255, 255, 255))
            screen.blit(t, t.get_rect(center=r.center))

        imports.pygame.display.flip()


def apply_move(screen, sq, board, piece, frm, to, current_player):
    """Apply a human move, handle promotion. Returns (new_board, promotion_choice_or_None)."""
    new_board = move_piece_on_board(piece, frm, to, board,
                                    update_ep=True, update_castling=True)
    new_r, new_c = sq_to_rc(to)
    if piece in ('WP', 'BP'):
        end_row = 0 if piece == 'WP' else 7
        if new_r == end_row:
            draw_board(screen, sq, board, frm, [], current_player, None, None)
            imports.pygame.display.flip()
            choice = show_promotion_menu(screen, sq, piece[0])
            new_board[new_r][new_c] = choice
    return new_board


def run_game(screen, mode):
    sq = imports.SQUARE_SIZE
    board = fresh_board()
    imports.board = board
    imports.en_passant_target = None
    imports.castling_rights = [True, True, True, True]

    current_player = 'W'
    selected_piece = None
    selected_pos   = None
    legal_moves    = []
    last_move      = None   # (from_pos, to_pos) of the most recent move
    premove        = None   # (piece, from_pos, to_pos) queued premove
    ai_thinking    = False
    ai_result      = [None]

    clock = imports.pygame.time.Clock()

    while True:
        clock.tick(60)

        # ── AI turn ───────────────────────────────────────────────────────────
        if mode == 'pvc' and current_player == AI_COLOR and not ai_thinking:
            ai_thinking = True
            ai_result[0] = None
            board_snapshot = copy.deepcopy(board)
            ep_snapshot = imports.en_passant_target
            cr_snapshot = list(imports.castling_rights)
            def ai_worker(b=board_snapshot, ep=ep_snapshot, cr=cr_snapshot):
                saved_ep = imports.en_passant_target
                saved_cr = list(imports.castling_rights)
                imports.en_passant_target = ep
                imports.castling_rights = list(cr)
                move = get_best_move(b, AI_COLOR, AI_DEPTH)
                imports.en_passant_target = saved_ep
                imports.castling_rights = saved_cr
                ai_result[0] = move
            threading.Thread(target=ai_worker, daemon=True).start()

        if ai_thinking and ai_result[0] is not None:
            ai_thinking = False
            move = ai_result[0]
            if move:
                piece, frm, to = move
                board = move_piece_on_board(piece, frm, to, board,
                                            update_ep=True, update_castling=True)
                imports.board = board
                last_move = (frm, to)
            current_player = 'W' if current_player == 'B' else 'B'

            # ── execute premove if one is queued ──────────────────────────────
            if premove:
                pm_piece, pm_frm, pm_to = premove
                premove = None
                # re-fetch piece at that square (board changed)
                actual_piece = imports.get_piece_at_clicked_pos(pm_frm, board)
                legal = get_all_legal_moves(current_player, board)
                if (actual_piece == pm_piece and
                        any(f == pm_frm and t == pm_to for _, f, t in legal)):
                    board = apply_move(screen, sq, board, pm_piece, pm_frm, pm_to, current_player)
                    imports.board = board
                    last_move = (pm_frm, pm_to)
                    current_player = 'B' if current_player == 'W' else 'W'
                # if illegal, premove is silently discarded

        # ── game-over check ───────────────────────────────────────────────────
        if is_checkmate(current_player, board):
            winner = "Black" if current_player == 'W' else "White"
            draw_board(screen, sq, board, None, [], current_player, last_move, None)
            imports.pygame.display.flip()
            return show_game_over(screen, f"{winner} wins!")

        if is_stalemate(current_player, board):
            draw_board(screen, sq, board, None, [], current_player, last_move, None)
            imports.pygame.display.flip()
            return show_game_over(screen, "Stalemate — Draw!")

        # ── events ────────────────────────────────────────────────────────────
        for event in imports.pygame.event.get():
            if event.type == imports.pygame.QUIT:
                return False

            # right-click cancels premove
            if event.type == imports.pygame.MOUSEBUTTONDOWN and event.button == 3:
                premove = None
                selected_piece = None
                selected_pos   = None
                legal_moves    = []
                continue

            if event.type != imports.pygame.MOUSEBUTTONDOWN or event.button != 1:
                continue

            mouse_pos = imports.pygame.mouse.get_pos()
            if mouse_pos[1] >= sq * 8:
                continue
            clicked = imports.mouse_to_board_coordinates(mouse_pos, sq)

            # ── it's the AI's turn: queue a premove ───────────────────────────
            if mode == 'pvc' and current_player == AI_COLOR and ai_thinking:
                player_color = 'W' if AI_COLOR == 'B' else 'B'
                piece_here = imports.get_piece_at_clicked_pos(clicked, board)

                if piece_here and piece_here[0] == player_color:
                    # selecting a piece to premove
                    selected_piece = piece_here
                    selected_pos   = clicked
                    premove        = None   # reset previous premove selection
                elif selected_piece and selected_pos and clicked != selected_pos:
                    # committing the premove destination
                    premove        = (selected_piece, selected_pos, clicked)
                    selected_piece = None
                    selected_pos   = None
                continue

            # ── normal turn ───────────────────────────────────────────────────
            if mode == 'pvc' and current_player == AI_COLOR:
                continue

            piece_here = imports.get_piece_at_clicked_pos(clicked, board)

            if piece_here and piece_here[0] == current_player:
                selected_piece = piece_here
                selected_pos   = clicked
                legal_moves    = [(p, f, t) for p, f, t in
                                  get_all_legal_moves(current_player, board)
                                  if f == clicked]
            else:
                if selected_piece and selected_pos:
                    valid = any(t == clicked for _, _, t in legal_moves)
                    if valid:
                        board = apply_move(screen, sq, board, selected_piece,
                                           selected_pos, clicked, current_player)
                        imports.board = board
                        last_move = (selected_pos, clicked)
                        current_player = 'B' if current_player == 'W' else 'W'

                selected_piece = None
                selected_pos   = None
                legal_moves    = []

        # ── draw ──────────────────────────────────────────────────────────────
        screen.fill((30, 30, 30))
        draw_board(screen, sq, board, selected_pos, legal_moves,
                   current_player, last_move,
                   (premove[1], premove[2]) if premove else None)
        draw_status(screen, sq, current_player, mode, ai_thinking, premove)
        imports.pygame.display.flip()


def main():
    imports.pygame.init()
    screen = imports.pygame.display.set_mode(
        (imports.SCREEN_WIDTH, imports.SCREEN_HEIGHT + 40))
    imports.pygame.display.set_caption("Chess")

    while True:
        mode = show_menu(screen)
        if not run_game(screen, mode):
            break

    imports.pygame.quit()
    imports.sys.exit()


if __name__ == '__main__':
    main()
