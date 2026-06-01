from piece import Piece
from Position import Position


class Pawn(Piece):

    def isValidMove(self, newPosition, board) -> bool:

        current = self.getPosition()

        col_current = current.getColumn()
        row_current = current.getRow()

        col_new = newPosition.getColumn()
        row_new = newPosition.getRow()

        direction = 1 if self.getColor() == 0 else -1

        # avancer
        if col_current == col_new:

            if row_new == row_current + direction:

                if board.getPiece(newPosition) is None:
                    return True

            start_row = 2 if self.getColor() == 0 else 7

            if (
                row_current == start_row
                and row_new == row_current + 2 * direction
            ):

                intermediate = Position(
                    col_current,
                    row_current + direction
                )

                if (
                    board.getPiece(intermediate) is None
                    and board.getPiece(newPosition) is None
                ):
                    return True

        # diagonale
        if abs(ord(col_new) - ord(col_current)) == 1:

            if row_new == row_current + direction:

                target = board.getPiece(newPosition)

                if (
                    target is not None
                    and target.getColor() != self.getColor()
                ):
                    return True

        return False

    def __str__(self):
        return "P"