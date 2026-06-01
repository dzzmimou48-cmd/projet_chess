from piece import Piece
from Position import Position


class King(Piece):

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

        if dx == 0 and dy == 0:
            return False

        if dx <= 1 and dy <= 1:

            target = board.getPiece(newPosition)

            if target is not None:
                if target.getColor() == self.getColor():
                    return False

            return True

        return False

    def __str__(self):
        return "K"