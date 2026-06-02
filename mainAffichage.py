from chess import Chess
from Position import Position
from player import Player
from aiplayer import AIPlayer


def init_players(game):
    print("\n=== Partie d'echecs ===")
    print("1 - Joueur contre joueur")
    print("2 - Joueur contre IA")

    mode = input("Mode de jeu : ")

    if mode == "2":
        name = input("Nom du joueur blanc : ")
        game._Chess__players = [
            Player(name, 0),
            AIPlayer("IA", 1)
        ]
    else:
        game._Chess__players = [
            Player(input("Nom du joueur blanc : "), 0),
            Player(input("Nom du joueur noir : "), 1)
        ]

    game._Chess__currentPlayer = game._Chess__players[0]


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

    print("\n      a  b  c  d  e  f  g  h")
    print("    +------------------------+")

    for row in range(8, 0, -1):
        line = f" {row}  |"

        for col in "abcdefgh":
            piece = board.getPiece(Position(col, row))

            if piece is None:
                line += " . "
            else:
                if piece.getColor() == 1:
                    symbol = white_symbols.get(str(piece).upper(), "?")
                else:
                    symbol = black_symbols.get(str(piece).upper(), "?")

                line += f" {symbol} "

        print(line + f"|  {row}")

    print("    +------------------------+")
    print("      a  b  c  d  e  f  g  h")
    print("Blancs : ♔ ♕ ♖ ♗ ♘ ♙   Noirs : ♚ ♛ ♜ ♝ ♞ ♟")
    print("Format d'un coup : e2 e4\n")


def display_turn(player):
    color = "Blancs" if player.getColor() == 0 else "Noirs"
    print(f"Au tour de {player.getName()} ({color})")


def display_invalid_move(player, attempts):
    if isinstance(player, AIPlayer):
        if attempts == 1:
            print("L'IA cherche un coup valide...")
        elif attempts % 25 == 0:
            print(f"L'IA continue sa recherche ({attempts} essais).")

        return

    print("Coup invalide. Exemple attendu : e2 e4\n")


def main():
    game = Chess()
    init_players(game)

    while True:
        display_board_pretty(game)

        move = ""
        attempts = 0
        player = game._Chess__currentPlayer
        display_turn(player)

        while not game.isValidMove(move):
            move = player.askMove()

            if not game.isValidMove(move):
                attempts += 1
                display_invalid_move(player, attempts)

        game.updateBoard(move)
        game.switchPlayer()


if __name__ == "__main__":
    main()
