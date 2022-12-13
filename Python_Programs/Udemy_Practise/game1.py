g = True
def gameon_choice():
    choice = input('Would you like to play the game? Y/N:')
    if choice == 'Y':
        game_on(g)
    else:
        print(f"Current list is: {game_list}")
        print("Thanks for playing!!!")

def game_on(g):
    while g:
        display_game(game_list)
        p = user_choice()
        replace_value(p)
        g = gameon_choice()

def display_game(game_list):
    print("Current list:")
    print(game_list)

def user_choice():
    p = -1
    while p not in range(0, len(game_list)):
        p = int(input("Enter position to replace:"))
        if p not in range(0, len(game_list)):
            print("Invalid. Position out of range.")
        else:
            pass
    return p

def replace_value(p):
    v = input(f"Enter value to be replaced in position {p}.")
    game_list[p] = v
    return game_list


game_list = [8,9,10,11]
gameon_choice()





