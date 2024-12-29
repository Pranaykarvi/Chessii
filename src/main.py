
import pygame
from board import Board
from pieces import Piece

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Chess Game")
clock = pygame.time.Clock()

# Load board and pieces
board = Board(screen)
pieces = [
    # White Pieces
    Piece("king", "white", (4, 7), r"D:\target\ml\chessii\assets\LightKing.webp"),
    Piece("queen", "white", (3, 7), r"D:\target\ml\chessii\assets\LightQueen.webp"),
    Piece("rook", "white", (0, 7), r"D:\target\ml\chessii\assets\LightRook.webp"),
    Piece("rook", "white", (7, 7), r"D:\target\ml\chessii\assets\LightRook.webp"),
    Piece("bishop", "white", (2, 7), r"D:\target\ml\chessii\assets\LightBishop.webp"),
    Piece("bishop", "white", (5, 7), r"D:\target\ml\chessii\assets\LightBishop.webp"),
    Piece("knight", "white", (1, 7), r"D:\target\ml\chessii\assets\LightKnight.webp"),
    Piece("knight", "white", (6, 7), r"D:\target\ml\chessii\assets\LightKnight.webp"),
    Piece("pawn", "white", (0, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (1, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (2, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (3, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (4, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (5, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (6, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),
    Piece("pawn", "white", (7, 6), r"D:\target\ml\chessii\assets\LightPawn.webp"),

    # Black Pieces
    Piece("king", "black", (4, 0), r"D:\target\ml\chessii\assets\DarkKing.webp"),
    Piece("queen", "black", (3, 0), r"D:\target\ml\chessii\assets\DarkQueen.webp"),
    Piece("rook", "black", (0, 0), r"D:\target\ml\chessii\assets\DarkRook.webp"),
    Piece("rook", "black", (7, 0), r"D:\target\ml\chessii\assets\DarkRook.webp"),
    Piece("bishop", "black", (2, 0), r"D:\target\ml\chessii\assets\DarkBishop.webp"),
    Piece("bishop", "black", (5, 0), r"D:\target\ml\chessii\assets\DarkBishop.webp"),
    Piece("knight", "black", (1, 0), r"D:\target\ml\chessii\assets\DarkKnight.webp"),
    Piece("knight", "black", (6, 0), r"D:\target\ml\chessii\assets\DarkKnight.webp"),
    Piece("pawn", "black", (0, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (1, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (2, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (3, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (4, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (5, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (6, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
    Piece("pawn", "black", (7, 1), r"D:\target\ml\chessii\assets\DarkPawn.webp"),
]


# Game state
selected_piece = None
target_position = None
tile_size = board.tile_size


def get_piece_at(position):
    """Get the piece at a given board position."""
    for piece in pieces:
        if piece.position == position:
            return piece
    return None


def is_valid_move(piece, new_position):
    """Validate if the move is legal according to chess rules."""
    x, y = piece.position
    nx, ny = new_position

    # Ensure new position is within the board
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        return False

    # Ensure new position is not occupied by a friendly piece
    target_piece = get_piece_at(new_position)
    if target_piece and target_piece.color == piece.color:
        return False

    dx, dy = nx - x, ny - y

    if piece.name == "pawn":
        if piece.color == "white":
            if dy == -1 and dx == 0 and not target_piece:  # Move forward
                return True
            if dy == -1 and abs(dx) == 1 and target_piece:  # Capture diagonally
                return True
            if y == 6 and dy == -2 and dx == 0 and not target_piece:  # Initial double move
                return True
        elif piece.color == "black":
            if dy == 1 and dx == 0 and not target_piece:  # Move forward
                return True
            if dy == 1 and abs(dx) == 1 and target_piece:  # Capture diagonally
                return True
            if y == 1 and dy == 2 and dx == 0 and not target_piece:  # Initial double move
                return True

    elif piece.name == "rook":
        if dx == 0 or dy == 0:  # Horizontal or vertical move
            return path_is_clear(piece.position, new_position)

    elif piece.name == "knight":
        if (abs(dx), abs(dy)) in [(2, 1), (1, 2)]:  # L-shape moves
            return True

    elif piece.name == "bishop":
        if abs(dx) == abs(dy):  # Diagonal move
            return path_is_clear(piece.position, new_position)

    elif piece.name == "queen":
        if dx == 0 or dy == 0 or abs(dx) == abs(dy):  # Rook + Bishop movement
            return path_is_clear(piece.position, new_position)

    elif piece.name == "king":
        if abs(dx) <= 1 and abs(dy) <= 1:  # One square in any direction
            return True

    return False


def path_is_clear(start, end):
    """Check if there are no pieces blocking the path between start and end."""
    sx, sy = start
    ex, ey = end
    dx = 1 if ex > sx else -1 if ex < sx else 0
    dy = 1 if ey > sy else -1 if ey < sy else 0

    x, y = sx + dx, sy + dy
    while (x, y) != (ex, ey):
        if get_piece_at((x, y)):
            return False
        x += dx
        y += dy
    return True



def move_piece(piece, new_position):
    """Move a piece to the new position and handle capturing."""
    global screen, pieces

    # Remove any piece at the target position (capturing)
    target_piece = get_piece_at(new_position)
    if target_piece and target_piece.color != piece.color:
        pieces.remove(target_piece)  # Remove captured piece

    # Animate the move
    start_x, start_y = piece.position
    end_x, end_y = new_position
    frames = 20
    for i in range(frames + 1):
        x = start_x + (end_x - start_x) * i / frames
        y = start_y + (end_y - start_y) * i / frames
        board.draw_board()
        for p in pieces:
            if p != piece:
                p.draw(screen, tile_size, board.board_position)
        piece.draw_at(screen, tile_size, board.board_position, (x, y))
        pygame.display.flip()
        clock.tick(60)
    
    # Update piece position
    piece.position = new_position



def main():
    global selected_piece
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                board_x = (mouse_x - board.board_position[0]) // tile_size
                board_y = (mouse_y - board.board_position[1]) // tile_size
                clicked_position = (board_x, board_y)

                if selected_piece:
                    # Try to move the selected piece
                    if is_valid_move(selected_piece, clicked_position):
                        move_piece(selected_piece, clicked_position)
                        selected_piece = None
                    else:
                        selected_piece = None  # Deselect if invalid
                else:
                    # Select a piece
                    selected_piece = get_piece_at(clicked_position)

        # Draw board and pieces
        board.draw_board()
        for piece in pieces:
            piece.draw(screen, tile_size, board.board_position)

        if selected_piece:
            # Highlight the selected piece
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (
                    board.board_position[0] + selected_piece.position[0] * tile_size,
                    board.board_position[1] + selected_piece.position[1] * tile_size,
                    tile_size,
                    tile_size,
                ),
                3,
            )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
