import chess-ui
import childPiece

# import sys
# sys.path.append('../../chess-ui')
# from chessboard_parts.tiles import Tiles
# from window import ChessWindow
# import pygame

# class Test_King(unittest.TestCase):
#     def setUp(self):

window = pygame.display.set_mode((0, 0))
tile_board = Tiles(window)
print(tile_board.tile_dict)

# class Test_King_move(Test_King):
#     def test_King_move(self):
#         self.assertEquals(self.wking.move_loc(0, King, tiles), [(1,3), (2,2), (3,3)])

    
#     #testing pawns ~ will move 2 spaces forward on first move, the move single square forward until they reach the end of the board