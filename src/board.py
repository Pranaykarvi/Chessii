import pygame

class Board:
    def __init__(self, screen, tile_size=80):
        self.screen = screen
        self.tile_size = tile_size
        self.board_image = pygame.image.load(r"D:\target\ml\chessii\assets\board2.png")
        self.board_image = pygame.transform.scale(self.board_image, (tile_size * 8, tile_size * 8))
        self.board_position = (
            (screen.get_width() - self.board_image.get_width()) // 2,
            (screen.get_height() - self.board_image.get_height()) // 2,
        )

    def draw_board(self):
        self.screen.blit(self.board_image, self.board_position)

