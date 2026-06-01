from piece import Piece
from Position import Position


class Knight(Piece):

    def isValidMove(self, newPosition, board) -> bool:

        current = self.getPosition()

        dx = abs(
            ord(newPosition.getColumn())
            - ord(current.getColumn())
        )

        dy = abs(
            newPosition.getRow()
            - current.getRow()
        )

        target = board.getPiece(newPosition)

        if target is not None:
            if target.getColor() == self.getColor():
                return False

        return (
            (dx == 2 and dy == 1)
            or
            (dx == 1 and dy == 2)
        )

    def __str__(self):
        return "N"