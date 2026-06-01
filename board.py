from Position import Position
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from pawn import Pawn


class Board:
    """Représente l'échiquier."""

    def __init__(self):
        self.__pieces = []
        self.__initPieces()

    def __initPieces(self) -> None:

        # Pièces blanches
        self.__pieces.append(Rook(Position("a", 1), 0))
        self.__pieces.append(Knight(Position("b", 1), 0))
        self.__pieces.append(Bishop(Position("c", 1), 0))
        self.__pieces.append(Queen(Position("d", 1), 0))
        self.__pieces.append(King(Position("e", 1), 0))
        self.__pieces.append(Bishop(Position("f", 1), 0))
        self.__pieces.append(Knight(Position("g", 1), 0))
        self.__pieces.append(Rook(Position("h", 1), 0))

        for col in "abcdefgh":
            self.__pieces.append(Pawn(Position(col, 2), 0))

        # Pièces noires
        self.__pieces.append(Rook(Position("a", 8), 1))
        self.__pieces.append(Knight(Position("b", 8), 1))
        self.__pieces.append(Bishop(Position("c", 8), 1))
        self.__pieces.append(Queen(Position("d", 8), 1))
        self.__pieces.append(King(Position("e", 8), 1))
        self.__pieces.append(Bishop(Position("f", 8), 1))
        self.__pieces.append(Knight(Position("g", 8), 1))
        self.__pieces.append(Rook(Position("h", 8), 1))

        for col in "abcdefgh":
            self.__pieces.append(Pawn(Position(col, 7), 1))

    def getPosition(self, piece):

        for current_piece in self.__pieces:
            if current_piece == piece:
                return current_piece.getPosition()

        return None

    def getPiece(self, position: Position):

        for piece in self.__pieces:
            if piece.getPosition() == position:
                return piece

        return None

    def getPieces(self):

        return self.__pieces

    def movePiece(self, old_position: Position, new_position: Position) -> bool:

        piece = self.getPiece(old_position)

        # aucune pièce
        if piece is None:
            return False

        # déplacement invalide
        if not piece.isValidMove(new_position, self):
            return False

        target = self.getPiece(new_position)

        # pièce alliée sur la case
        if target is not None:

            if target.getColor() == piece.getColor():
                return False

            # capture
            self.__pieces.remove(target)

        # déplacement
        piece.setPosition(new_position)

        return True


if __name__ == "__main__":

    board = Board()

    print("Nombre de pièces :", len(board.getPieces()))

    print("Pièce en e1 :", board.getPiece(Position("e", 1)))

    print("Pièce en d8 :", board.getPiece(Position("d", 8)))

    print("Test Board OK !")