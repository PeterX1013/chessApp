from piece import Piece


class Rook(Piece):
    def __init__(self, pMove, pPoints, pColor):
        self.move = pMove
        self.points = pPoints
        self.color = pColor
