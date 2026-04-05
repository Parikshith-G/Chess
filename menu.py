import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

BG_COLOR = (30, 30, 30)
BTN_COLOR = (70, 130, 180)
BTN_HOVER = (100, 160, 210)
TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (255, 215, 0)


def draw_button(screen, rect, text, font, hovered):
    color = BTN_HOVER if hovered else BTN_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=10)
    label = font.render(text, True, TEXT_COLOR)
    screen.blit(label, label.get_rect(center=rect.center))


def show_menu(screen):
    """Show mode selection. Returns 'pvp' or 'pvc'."""
    font_title = pygame.font.Font(None, 90)
    font_btn = pygame.font.Font(None, 52)

    pvp_rect = pygame.Rect(SCREEN_WIDTH // 2 - 180, 380, 360, 80)
    pvc_rect = pygame.Rect(SCREEN_WIDTH // 2 - 180, 500, 360, 80)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pvp_rect.collidepoint(mx, my):
                    return 'pvp'
                if pvc_rect.collidepoint(mx, my):
                    return 'pvc'

        screen.fill(BG_COLOR)
        title = font_title.render("CHESS", True, TITLE_COLOR)
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 220)))

        sub = pygame.font.Font(None, 38).render("Select Game Mode", True, (200, 200, 200))
        screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, 310)))

        draw_button(screen, pvp_rect, "Player vs Player", font_btn, pvp_rect.collidepoint(mx, my))
        draw_button(screen, pvc_rect, "Player vs Computer", font_btn, pvc_rect.collidepoint(mx, my))

        pygame.display.flip()


def show_game_over(screen, message):
    """Show game over screen. Returns True to play again, False to quit."""
    font_big = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 44)

    again_rect = pygame.Rect(SCREEN_WIDTH // 2 - 160, 480, 320, 70)
    quit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 160, 580, 320, 70)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if again_rect.collidepoint(mx, my):
                    return True
                if quit_rect.collidepoint(mx, my):
                    return False

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))

        msg = font_big.render(message, True, TITLE_COLOR)
        screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, 340)))

        draw_button(screen, again_rect, "Play Again", font_small, again_rect.collidepoint(mx, my))
        draw_button(screen, quit_rect, "Quit", font_small, quit_rect.collidepoint(mx, my))

        pygame.display.flip()
