import random


def game_is_on():
    print("Welcome to tic-tac-toe")
    print('Positions to choose in order:')
    print('-------')
    print('|0|1|2|')
    print('-------')
    print('|3|4|5|')
    print('-------')
    print('|6|7|8|')
    print('-------')
    b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_game(b)
    choice = {'P1': ' ', 'P2': ' '}
    p = pick_player()
    player_choice(choice)
    game_on = True
    while game_on:
        if p == 'P1':
            pos = gamer_position(p, b)
            v = position_value(choice, pos, p, b)
            display_game(b)
            if check_win(v, b):
                display_game(b)
                print(f"Congrats!!! Winner is {p}")
                game_on = False
            else:
                if board_full(b):
                    display_game(b)
                    print(f"Oops!!! It's a tie.")
                    game_on = False
                else:
                    p = 'P2'
        else:
            pos = gamer_position(p, b)
            v = position_value(choice, pos, p, b)
            display_game(b)
            if check_win(v, b):
                display_game(b)
                print(f"Congrats!!! Winner is {p}")
                game_on = False
            else:
                if board_full(b):
                    display_game(b)
                    print(f"Oops!!! It's a tie.")
                    game_on = False
                else:
                    p = 'P1'

    if game_restart():
        game_is_on()


def pick_player():
    if random.randint(1, 2) == 1:
        p = 'P1'
        print("Player1's turn first")
    else:
        p = 'P2'
        print("Player2's turn first")
    return p


def player_choice(choice):
    while choice['P1'] != '0' and choice['P1'] != 'X':
        choice['P1'] = str(input(f"Player1's choice '0' or 'X'?:"))
        if choice['P1'] != '0' and choice['P1'] != 'X':
            print("Invalid choice")
        else:
            if choice['P1'] == '0':
                choice['P2'] = 'X'
            elif choice['P1'] == 'X':
                choice['P2'] = '0'
    print(f"Player2 choice is {choice['P2']} by default.")


def gamer_position(p, b):
    pos = int(input(f"Enter position for {p}:"))
    while b[pos] == 'X' or b[pos] == '0':
        pos = int(input('Invalid. Position already filled!!!:'))
    else:
        return int(pos)


def position_value(choice, pos, p, b):
    b[pos] = choice[p]
    return b[pos]


def check_win(v, b):
    if b[0] == b[1] == b[2] == v or b[3] == b[4] == b[5] == v or b[6] == b[7] == b[8] == v or\
            b[0] == b[3] == b[6] == v or b[1] == b[4] == b[7] == v or b[2] == b[5] == b[8] == v or \
            b[0] == b[4] == b[8] == v or b[6] == b[4] == b[2] == v:
        return True


def board_full(b):
    for index in range(0, len(b)):
        if b[index] == ' ':
            return False
    return True


def game_restart():
    r = input('Enter Y/N to restart/stop next game:')
    if r == 'Y':
        return True
    else:
        return False


def display_game(b):
    print('-------')
    print('|' + b[0] + '|' + b[1] + '|' + b[2] + '|')
    print('-------')
    print('|' + b[3] + '|' + b[4] + '|' + b[5] + '|')
    print('-------')
    print('|' + b[6] + '|' + b[7] + '|' + b[8] + '|')
    print('-------')


game_is_on()
