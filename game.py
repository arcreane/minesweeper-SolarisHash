from gameLogic import create_grid, display_grid, set_difficulty


def start_game():

    width, height = set_difficulty()

    grid = create_grid(width, height)

    display_grid(grid)

