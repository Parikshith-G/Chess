# Chess

A Python/Pygame chess game with Player vs Player and Player vs Computer modes.

## Features

- **PvP** — two players on the same machine
- **PvC** — play against a minimax AI with alpha-beta pruning (plays Black)
- Full move validation for all pieces
- Castling (kingside & queenside)
- En passant
- Pawn promotion (choose Queen, Rook, Bishop, or Knight)
- Checkmate & stalemate detection
- Legal move highlighting (green dots)
- Last move highlight (light green squares)
- King in check highlight (red)
- Premove support in PvC mode — queue a move while the AI is thinking, right-click to cancel
- Game over screen with play again option

## Requirements

- Python 3.10+
- pygame

```bash
pip install pygame
```

## Running

```bash
cd Chess
python chess.py
```

## Project Structure

```
Chess/
├── chess.py                  # Main game loop
├── ai.py                     # Minimax engine with alpha-beta pruning
├── game_logic.py             # Board-agnostic move validation & game state
├── menu.py                   # Mode selection & game over screens
├── imports.py                # Centralised imports & global state
├── board_related_items.py    # Board state, piece mappings, blueprint
├── check_valid_movement.py   # Move validation dispatcher
├── constants.py              # Screen dimensions
├── beams/                    # Attack map generation (check detection)
├── valid_movements/          # Per-piece movement rules
│   ├── white/
│   ├── black/
│   └── movements/
├── is_king_checked/          # Check detection
├── piece_white/              # White piece images
└── piece_black/              # Black piece images
```

## AI

The computer uses minimax search with alpha-beta pruning at depth 3, evaluated with material values and piece-square positional tables. Estimated strength: ~600–900 ELO.
