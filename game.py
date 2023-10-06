from gameLogic import create_grid, display_grid, set_difficulty


def start_game():

    width, height, mines = set_difficulty()

    grid = create_grid(width, height, mines)

    display_grid(grid)

