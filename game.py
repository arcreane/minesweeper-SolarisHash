from gameLogic import create_grid


check_digit = True
while(check_digit):
    try:
        width_choice = int(input("Enter field width : "))
        height_choice = int(input("Enter field height : "))
        check_digit = False
    except ValueError:
        print("Entré une valeur numérique")

nb_collumn = 0
nb_row = 0

grid = create_grid(width_choice, height_choice)
for line in grid:
    print(line)
