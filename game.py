from gameLogic import create_grid, display_grid, set_difficulty, display_grid2


def start_game():

    width, height, mines = set_difficulty()

    grid, grid_for_game = create_grid(width, height, mines)

    display_grid(grid)
    display_grid2(grid,grid_for_game)




