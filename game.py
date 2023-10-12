from gameLogic import create_grid, display_grid, set_difficulty, display_grid2, decouvrir_case, put_flag


def start_game():
    new_game = True

    while new_game:
        width, height, mines = set_difficulty()

        cells_without_mines = width * height - mines

        grid, grid_for_game = create_grid(width, height, mines)

        display_grid(grid)
        display_grid2(grid, grid_for_game)

        flagged_cells = set()  # Utilisé pour suivre les cellules marquées

        while True:
            if cells_without_mines == 0:
                print("Félicitations ! Vous avez gagné !")
                break
            try:
                action = input("Retourner une case (u) ou placer un flag (f) :").lower()

                if action == 'u':
                    try:
                        x = int(input("Entrez la colonne : "))
                        y = int(input("Entrez la rangée : "))
                    except ValueError:
                        print("Veuillez entrer des nombres valides.")
                        continue

                    if 0 <= x < width and 0 <= y < height:
                        if (x, y) in flagged_cells:
                            print("Vous avez flagger cellule, vous ne pouvez donc plus la selectionner")
                        elif grid[y][x] == '*':
                            print("Boom ! Vous avez touché une mine. Fin du jeu.")
                            break
                        else:
                            decouvrir_case(grid, grid_for_game, x, y, cells_without_mines)
                            display_grid(grid)
                            display_grid2(grid, grid_for_game)
                    else:
                        print("Coordonnées non valides.")
                elif action == 'f':
                    try:
                        x = int(input("Entrez la colonne : "))
                        y = int(input("Entrez la rangée : "))
                    except ValueError:
                        print("Veuillez entrer des nombres valides.")
                        continue

                    if 0 <= x < width and 0 <= y < height:
                        put_flag(grid_for_game, x, y)
                        flagged_cells.add((x, y))
                        display_grid(grid)
                        display_grid2(grid, grid_for_game)
                    else:
                        print("Coordonnées non valide")
            except ValueError:
                print("Entrer une action valide")

        print("Do you want to play a new game")
        choice = int(input("1.Yes\t2.No"))
        if choice == 2:
            new_game = False