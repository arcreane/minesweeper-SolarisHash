import os
import random


def set_difficulty():
    check_digit = True
    while check_digit:
        try:
            print("Choose your difficulty")
            difficulty = int(input("1.Easy\t2.Medium\t3.Hard\n"))
            match difficulty:
                case 1:
                    return 9, 9
                case 2:
                    return 16, 16
                case 3:
                    return 30, 16
        except ValueError:
            print("Choose a right choice")


def create_grid(width, height):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    return grid


def display_grid(grid):
    for index, line in enumerate(grid):
        print(f"{index:>2} {line}")
