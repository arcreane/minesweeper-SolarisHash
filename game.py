from gameLogic import create_grid, display_grid, set_difficulty, display_grid2, decouvrir_case


def start_game():

    width, height, mines = set_difficulty()

    grid, grid_for_game = create_grid(width, height, mines)

    display_grid(grid)
    display_grid2(grid,grid_for_game)

    while True:
        try:
            x = int(input("Entrez la colonne : "))
            y = int(input("Entrez la rangée : "))
        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        if 0 <= x < width and 0 <= y < height:
            if grid[y][x] == '*':
                print("Boom ! Vous avez touché une mine. Fin du jeu.")
                break
            else:
                decouvrir_case(grid, grid_for_game, x, y)
                display_grid2(grid, grid_for_game)
        else:
            print("Coordonnées non valides.")




