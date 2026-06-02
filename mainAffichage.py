from chess import Chess
from Position import Position


def display_board_pretty(game):
    # accès au board (hack nécessaire sans modifier Chess)
    board = game._Chess__board

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
                symbol = str(piece)

                if piece.getColor() == 1:
                    symbol = symbol.lower()

                line += f" {symbol} |"
        print(line + f" {row}")
        print("  +---+---+---+---+---+---+---+---+")

    print("    a   b   c   d   e   f   g   h")
    print("Blancs : majuscules | Noirs : minuscules")
    print("Format attendu : e2 e4\n")


def display_invalid_move(player, attempts):
    if player.getName().upper() == "AI":
        if attempts == 1:
            print("IA : recherche d'un coup valide...")
        elif attempts % 25 == 0:
            print(f"IA : {attempts} tentatives analysees...")

        return

    print("Coup invalide. Essayez encore avec le format e2 e4.\n")


def main():
    game = Chess()
    game.initPlayers()

    while True:
        display_board_pretty(game)

        move = ""
        attempts = 0
        player = game._Chess__currentPlayer
        color_name = "Blancs" if player.getColor() == 0 else "Noirs"
        print(f"Tour de {player.getName()} ({color_name})")

        while not game.isValidMove(move):
            move = game._Chess__currentPlayer.askMove()

            if not game.isValidMove(move):
                attempts += 1
                display_invalid_move(player, attempts)

        game.updateBoard(move)
        game.switchPlayer()


if __name__ == "__main__":
    main()
