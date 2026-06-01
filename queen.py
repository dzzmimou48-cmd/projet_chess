from piece import Piece
from Position import Position


class Queen(Piece):

    def isValidMove(self, newPosition, board) -> bool:

        current = self.getPosition()

        col_current = ord(current.getColumn())
        row_current = current.getRow()

        col_new = ord(newPosition.getColumn())
        row_new = newPosition.getRow()

        dx = col_new - col_current
        dy = row_new - row_current

        if dx == 0 and dy == 0:
            return False

        # vertical
        if col_current == col_new:

            step = 1 if dy > 0 else -1

            for r in range(row_current + step, row_new, step):

                if board.getPiece(Position(chr(col_current), r)) is not None:
                    return False

        # horizontal
        elif row_current == row_new:

            step = 1 if dx > 0 else -1

            for c in range(col_current + step, col_new, step):

                if board.getPiece(Position(chr(c), row_current)) is not None:
                    return False

        # diagonale
        elif abs(dx) == abs(dy):

            step_col = 1 if dx > 0 else -1
            step_row = 1 if dy > 0 else -1

            for i in range(1, abs(dx)):

                col = chr(col_current + i * step_col)
                row = row_current + i * step_row

                if board.getPiece(Position(col, row)) is not None:
                    return False

        else:
            return False

        target = board.getPiece(newPosition)

        if target is not None:
            if target.getColor() == self.getColor():
                return False

        return True

    def __str__(self):
        return "Q"