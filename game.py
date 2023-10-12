import os
import time

from gameLogic import create_grid, display_grid, set_difficulty, display_grid2, decouvrir_case, put_flag, \
    count_discovered_cells, format_time


def start_game():
    new_game = True

    while new_game:
        width, height, mines = set_difficulty()

        cells_without_mines = width * height - mines

        grid, grid_for_game = create_grid(width, height, mines)

        display_grid(grid)
        display_grid2(grid, grid_for_game)

        flagged_cells = set()  # Utilisé pour suivre les cellules marquées
        start_time = time.time()

        while True:
            elapsed_time = int(time.time() - start_time)
            formatted_time = format_time(elapsed_time)
            print(f"Time elapsed: {formatted_time}")
            if cells_without_mines == 0:
                print("""░█▀▀░█▀█░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█░█░█░░░█▀█░▀█▀░▀█▀░█▀█░█▀█░░░█░░░█░█░█▀█░█░█░░░█░█░▀█▀░█▀█░░░█
░█░░░█░█░█░█░█░█░█▀▄░█▀█░░█░░█░█░█░░░█▀█░░█░░░█░░█░█░█░█░░░▀░░░░█░░█░█░█░█░░░█▄█░░█░░█░█░░░▀
░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░▀░░░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░░░▀""")
                print(f"You win in {elapsed_time} seconds")
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
                            print("""██████╗  ██████╗  ██████╗ ███╗   ███╗██╗    ██╗   ██╗ ██████╗ ██╗   ██╗██╗   ██╗███████╗    ██╗  ██╗██╗████████╗     █████╗     ███╗   ███╗██╗███╗   ██╗███████╗        ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗     ██╗██╗
██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║██║    ╚██╗ ██╔╝██╔═══██╗██║   ██║██║   ██║██╔════╝    ██║  ██║██║╚══██╔══╝    ██╔══██╗    ████╗ ████║██║████╗  ██║██╔════╝       ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    ██║██║
██████╔╝██║   ██║██║   ██║██╔████╔██║██║     ╚████╔╝ ██║   ██║██║   ██║██║   ██║█████╗      ███████║██║   ██║       ███████║    ██╔████╔██║██║██╔██╗ ██║█████╗         ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝    ██║██║
██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║╚═╝      ╚██╔╝  ██║   ██║██║   ██║╚██╗ ██╔╝██╔══╝      ██╔══██║██║   ██║       ██╔══██║    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝         ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗    ╚═╝╚═╝
██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██╗       ██║   ╚██████╔╝╚██████╔╝ ╚████╔╝ ███████╗    ██║  ██║██║   ██║       ██║  ██║    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    ██╗██╗
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝       ╚═╝    ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝    ╚═╝  ╚═╝╚═╝   ╚═╝       ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝""")
                            print(f"Time elapsed: {formatted_time}")
                            break
                        else:
                            decouvrir_case(grid, grid_for_game, x, y)
                            display_grid(grid)
                            display_grid2(grid, grid_for_game)
                            discovered_cells = count_discovered_cells(grid_for_game)
                            cells_without_mines -= discovered_cells
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