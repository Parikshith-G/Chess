import imports

SCREEN_WIDTH,SCREEN_HEIGHT=960,960

BOARD_SIZE=8
SQUARE_SIZE=SCREEN_HEIGHT//BOARD_SIZE

BLACK_PAWN_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_black/black_pawn.png'),(SQUARE_SIZE,SQUARE_SIZE))
BLACK_ROOK_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_black/black_rook.png'),(SQUARE_SIZE,SQUARE_SIZE))
BLACK_BISHOP_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_black/black_bishop.png'),(SQUARE_SIZE,SQUARE_SIZE))
BLACK_KING_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_black/black_king.png'),(SQUARE_SIZE,SQUARE_SIZE))
BLACK_KNIGHT_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_black/black_knight.png'),(SQUARE_SIZE,SQUARE_SIZE))
BLACK_QUEEN_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_black/black_queen.png'),(SQUARE_SIZE,SQUARE_SIZE))

WHITE_PAWN_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_white/white_pawn.png'),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_ROOK_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_white/white_rook.png'),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_BISHOP_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_white/white_bishop.png'),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_KING_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_white/white_king.png'),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_KNIGHT_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_white/white_knight.png'),(SQUARE_SIZE,SQUARE_SIZE))
WHITE_QUEEN_IMAGE=imports.pygame.transform.scale(imports.pygame.image.load('./piece_white/white_queen.png'),(SQUARE_SIZE,SQUARE_SIZE))
