# Projet Chess

Projet Python de jeu d'echecs en console realise dans un cadre pedagogique.

Le projet propose une architecture orientee objet avec un echiquier, des pieces, des joueurs humains et une IA simple. Une interface console amelioree est disponible pour afficher les pieces avec des symboles d'echecs.

## Fonctionnalites

- Plateau d'echecs initialise avec les pieces blanches et noires.
- Deplacements de base des pieces principales :
  - roi ;
  - dame ;
  - tour ;
  - fou ;
  - cavalier ;
  - pion.
- Verification des coups selon le type de piece.
- Gestion des captures.
- Alternance des tours entre les deux joueurs.
- Mode joueur contre joueur.
- Mode joueur contre IA dans `mainAffichage.py`.
- Affichage console simple avec `main.py`.
- Affichage console ameliore avec `mainAffichage.py`.

## Lancement

Depuis le dossier du projet :

```bash
python3 main.py
```

Pour lancer la version avec affichage ameliore et choix du mode de jeu :

```bash
python3 mainAffichage.py
```

## Format des coups

Les coups doivent etre saisis avec deux positions separees par un espace :

```text
e2 e4
```

La premiere position correspond a la case de depart, la deuxieme a la case d'arrivee.

## Mode IA

Dans `mainAffichage.py`, le programme propose :

```text
1 - Joueur contre joueur
2 - Joueur contre IA
```

En mode IA, le joueur humain joue les blancs et l'IA joue les noirs.

L'IA actuelle est volontairement simple : elle genere des coups aleatoires jusqu'a obtenir un coup valide.

## Structure du projet

```text
.
|-- main.py              # Point d'entree principal
|-- mainAffichage.py     # Interface console amelioree
|-- chess.py             # Gestion globale de la partie
|-- board.py             # Gestion de l'echiquier et des pieces
|-- Position.py          # Representation d'une case
|-- piece.py             # Classe abstraite des pieces
|-- player.py            # Joueur humain
|-- aiplayer.py          # Joueur IA
|-- king.py              # Regles du roi
|-- queen.py             # Regles de la dame
|-- rook.py              # Regles de la tour
|-- bishop.py            # Regles du fou
|-- knight.py            # Regles du cavalier
|-- pawn.py              # Regles du pion
`-- test_position.py     # Tests unitaires de Position
```

## Architecture

Le projet utilise une architecture orientee objet.

- `Chess` orchestre la partie : joueurs, tour courant, validation et boucle de jeu.
- `Board` stocke les pieces et applique les deplacements.
- `Position` represente une case de l'echiquier.
- `Piece` est une classe abstraite commune aux pieces.
- Chaque piece possede sa propre methode `isValidMove`.
- `Player` represente un joueur humain.
- `AIPlayer` herite de `Player` et genere automatiquement des coups.

## Tests

Pour lancer les tests unitaires :

```bash
python3 -m unittest
```

Pour verifier la syntaxe d'un fichier :

```bash
python3 -m py_compile mainAffichage.py
```

## Bibliotheques utilisees

Le projet utilise uniquement des bibliotheques standard de Python :

- `abc` : creation de la classe abstraite `Piece`.
- `random` : generation des coups de l'IA.
- `unittest` : tests unitaires.

Aucune dependance externe n'est necessaire.

## Limites connues

Le projet ne gere pas encore toutes les regles avancees des echecs :

- echec ;
- echec et mat ;
- roque ;
- promotion du pion ;
- prise en passant ;
- pat ;
- IA strategique.

Ces elements peuvent etre ajoutes dans de futures ameliorations.

## Contributions recentes

- Ajout d'un affichage ameliore dans `mainAffichage.py`.
- Ajout d'un mode joueur contre IA.
- Ajout des symboles de pieces blanches et noires.
- Amelioration de la lisibilite de `knight.py` avec une condition explicite `if not`.

## Auteur

Projet realise dans le cadre d'un travail scolaire a l'ISEP.
