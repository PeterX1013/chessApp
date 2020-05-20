from piece import Piece


class King(Piece):
    def __init__(self, pMove, pPoints, pColor):
        self.move = pMove
        self.points = pPoints
        self.color = pColor
