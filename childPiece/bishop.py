from parentPiece.piece import Piece


class Bishop(Piece):
    def __init__(self, pMove, pPoints, pColor):
        self.move = pMove
        self.points = pPoints
        self.color = pColor
