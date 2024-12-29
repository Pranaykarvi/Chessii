import pygame

class Piece:
    def __init__(self, name, color, position, image_path):
        self.name = name
        self.color = color
        self.position = position
        self.image = pygame.image.load(image_path)

    def draw(self, screen, tile_size, board_position):
        x, y = self.position
        scaled_image = pygame.transform.scale(self.image, (tile_size, tile_size))
        screen.blit(
            scaled_image,
            (board_position[0] + x * tile_size, board_position[1] + y * tile_size),
        )

    def draw_at(self, screen, tile_size, board_position, position):
        """Draw the piece at a specific position (for animation)."""
        x, y = position
        scaled_image = pygame.transform.scale(self.image, (tile_size, tile_size))
        screen.blit(
            scaled_image,
            (board_position[0] + x * tile_size, board_position[1] + y * tile_size),
        )
