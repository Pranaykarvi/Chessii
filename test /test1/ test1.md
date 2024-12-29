# Chess Game Prototype - v1

This is a functional prototype of a chess game implemented in Python using Pygame. The prototype focuses on rendering a chessboard, managing pieces, and allowing basic movements with capture logic. The application is designed for further enhancements, including rule validation and advanced game mechanics.

## Features

### Chessboard Rendering:
- A visually appealing 8x8 chessboard is drawn dynamically on the screen.

### Piece Management:
- Includes all standard chess pieces for both white and black sides.
- Each piece is rendered with respective images for easy identification.

### Basic Move Functionality:
- Allows movement of chess pieces across the board.
- Includes valid moves for each type of piece (e.g., pawns, knights, bishops).

### Capture Logic:
- Pieces of opposing colors can be captured.
- Captured pieces are removed from the game.

### Animations:
- Smooth animations for piece movement enhance the user experience.

## Installation and Setup

### Clone the repository:
```bash
git clone <repository-url>
cd chess-game
```

## Known Issues
### Move Validation:
- While basic rules are implemented, more advanced chess rules (e.g., castling, en passant) are not yet supported.
### Game Over Detection:
- Currently, the game does not detect checkmate or stalemate conditions.
### Highlighting Moves:
- Visual indicators for valid moves are not implemented.
## Future Improvements
- Add comprehensive chess rule validation.
- Implement advanced mechanics like castling, en passant, and pawn promotion.
- Introduce a game state manager for turn-based play.
- Enhance the UI with move highlights and player indicators.


Feel free to contribute or raise issues to improve this project! 😊
