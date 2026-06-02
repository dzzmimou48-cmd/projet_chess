from chess import Chess
from Position import Position


def display_board_pretty(game):
    # accès au board (hack nécessaire sans modifier Chess)
    board = game._Chess__board

    white_symbols = {
        "K": "♔", "Q": "♕", "R": "♖",
        "B": "♗", "N": "♘", "P": "♙"
    }

    black_symbols = {
        "K": "♚", "Q": "♛", "R": "♜",
        "B": "♝", "N": "♞", "P": "♟"
    }

    print("\n" + "-" * 39)
    print("              ECHIQUIER")
    print("-" * 39)
    print("    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")

    for row in range(8, 0, -1):
        line = str(row) + " |"
        for col in "abcdefgh":
            piece = board.getPiece(Position(col, row))

            if piece is None:
                line += " . |"
            else:
                if piece.getColor() == 1:
                    symbol = black_symbols.get(str(piece).upper(), "?")
                else:
                    symbol = white_symbols.get(str(piece).upper(), "?")

                line += f" {symbol} |"
        print(line + f" {row}")
        print("  +---+---+---+---+---+---+---+---+")

    print("    a   b   c   d   e   f   g   h")
    print("Blancs : ♔ ♕ ♖ ♗ ♘ ♙ | Noirs : ♚ ♛ ♜ ♝ ♞ ♟")
    print("Format attendu : e2 e4\n")


def main():
    game = Chess()
    game.initPlayers()

    while True:
        display_board_pretty(game)

        move = ""
        while not game.isValidMove(move):
            player = game._Chess__currentPlayer
            color_name = "Blancs" if player.getColor() == 0 else "Noirs"
            print(f"Tour de {player.getName()} ({color_name})")
            move = game._Chess__currentPlayer.askMove()

            if not game.isValidMove(move):
                print("Coup invalide. Essayez encore avec le format e2 e4.\n")

        game.updateBoard(move)
        game.switchPlayer()


if __name__ == "__main__":
    main()
