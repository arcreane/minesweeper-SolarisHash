from gameLogic import create_grid, display_grid, set_difficulty, display_grid2, decouvrir_case, put_flag, \
    count_discovered_cells


def start_game():
    new_game = True

    while new_game:
        width, height, mines = set_difficulty()

        cells_without_mines = width * height - mines
        print(cells_without_mines)

        grid, grid_for_game = create_grid(width, height, mines)

        display_grid(grid)
        display_grid2(grid, grid_for_game)

        flagged_cells = set()  # Utilisé pour suivre les cellules marquées

        while True:
            if cells_without_mines == 0:
                print("""
                ░█▀▀░█▀█░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█░█░█░░░█▀█░▀█▀░▀█▀░█▀█░█▀█░░░█░░░█░█░█▀█░█░█░░░█░█░▀█▀░█▀█░░░█
░█░░░█░█░█░█░█░█░█▀▄░█▀█░░█░░█░█░█░░░█▀█░░█░░░█░░█░█░█░█░░░▀░░░░█░░█░█░█░█░░░█▄█░░█░░█░█░░░▀
░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░▀░░░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░░░▀
                """)
                break
            try:
                action = input("Flip a square (u) or place a flag (f) :").lower()

                if action == 'u':
                    try:
                        x = int(input("Enter column : "))
                        y = int(input("Enter row : "))
                    except ValueError:
                        print("Enter a valid number.")
                        continue

                    if 0 <= x < width and 0 <= y < height:
                        if (x, y) in flagged_cells:
                            print("You have flagged this cell, so you can no longer select it.")
                        elif grid[y][x] == '*':
                            print("Boom! You've hit a mine. Game over !!")
                            break
                        else:
                            decouvrir_case(grid, grid_for_game, x, y, cells_without_mines)
                            display_grid(grid)
                            display_grid2(grid, grid_for_game)
                            discovered_cells = count_discovered_cells(grid_for_game)
                            cells_without_mines -= discovered_cells
                            print(cells_without_mines)
                    else:
                        print("Invalid coordinates.")
                elif action == 'f':
                    try:
                        x = int(input("Enter column : "))
                        y = int(input("Enter row : "))
                    except ValueError:
                        print("Please enter valid numbers.")
                        continue

                    if 0 <= x < width and 0 <= y < height:
                        put_flag(grid_for_game, x, y)
                        flagged_cells.add((x, y))
                        display_grid(grid)
                        display_grid2(grid, grid_for_game)
                    else:
                        print("Invalid coordinates")
            except ValueError:
                print("Enter a valid action")

        print("Do you want to play a new game")
        choice = int(input("1.Yes\t2.No"))

        if choice == 2:
            new_game = False