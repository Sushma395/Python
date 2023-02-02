import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10
          , 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f'{self.suit} : {self.rank} : {self.value}'


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_card(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop(0)


class Player:
    def __init__(self, name, money=100):
        self.cards = []
        self.name = name
        print(f'Player Name: {name}')
        self.money = money
        self.bet = 0

    def total_money(self):
        print(f"{self.name}'s total money: {self.money}")

    def bet_money(self):
        self.bet = int(input(f"Enter {self.name}'s bet:"))
        while self.bet > self.money:
            print('Bet higher than money!!')
            self.bet = int(input(f"Enter {self.name}'s bet:"))
        else:
            self.money -= self.bet
        return self.bet

    def change_money(self, change):
        self.money += (change * self.bet)
        return self.total_money()

    def add_card(self, new_card):
        self.cards.append(new_card)
        if self.name == 'Dealer' and len(self.cards) == 2:
            print(f"***Dealer's card 2 details: Hidden***")
        else:
            print(f"***{self.name}'s card {len(self.cards)} details: {self.cards[-1]} ***")
        self.cards_value()

    def cards_value(self):
        count_ace = 0
        sum_cards = 0
        for word in self.cards:
            sum_cards += word.value
            if word.rank == 'Ace':
                count_ace += 1

        if sum_cards > 21 and count_ace > 0:
            if sum_cards >= (count_ace*11+10):
                sum_cards = sum_cards - (count_ace * 10)
                print(f"{self.name} count of Ace: {count_ace}.Considered {count_ace} ace as 1 ")
            elif (count_ace*11+10) > sum_cards:
                sum_cards = sum_cards - ((count_ace-1)*10)
                print(f"{self.name} count of Ace: {count_ace}.Considered {count_ace-1} ace as 1 ")
            else:
                pass
        return sum_cards


def player_check():
    if P1.cards_value() < 21:
        P1.cards_value()
        player_action()
        dealer_check()
    elif P1.cards_value() == 21:
        print(f'-----{P1.name} Wins!!!!-----')
        P1.change_money(change=1.5)
        D1.change_money(change=-0.5)
    else:
        print('------Bust------')
        print(f'-----{P1.name} Looses!!!-----')
        P1.change_money(change=0)
        D1.total_money()


def player_action():
    action = input(f"{P1.name} has sum < 21. Choose STAY or HIT? ").upper()
    while action != 'HIT' and action != 'STAY':
        action = input(f"ERROR!!! {P1.name} has sum < 21. Choose STAY or HIT? ").upper()
    else:
        if action == 'HIT':
            P1.add_card(D.deal_card())
            player_check()
        if action == 'STAY':
            print(f"Show {D1.name}'s hidden card: {D1.cards[-1]}")
            D1.cards_value()


def dealer_check():
    if D1.cards_value() == 21:
        print(f'-----{D1.name} Wins!!!!-----')
        P1.total_money()
        D1.total_money()
    elif D1.cards_value() > 21:
        print(f'------BUST------')
        print(f'-----{D1.name} Looses!!!!-----')
        P1.change_money(change=2)
        D1.change_money(change=-1)
    else:
        if D1.cards_value() >= 17:
            print(f"{D1.name}'s sum is {D1.cards_value()}: STAY")
            if P1.cards_value() < D1.cards_value():
                print(f'-----{P1.name} Looses!!!!-----')
                P1.total_money()
                D1.total_money()
            elif P1.cards_value() > D1.cards_value():
                print(f'-----{P1.name} Wins!!!!-----')
                P1.change_money(change=2)
                D1.change_money(change=-1)
            else:
                print(f'-----TIE-----')
                P1.change_money(change=1)
                D1.change_money(change=-1)
        else:
            D1.add_card(D.deal_card())
            D1.total_money()
            dealer_check()


game_on = True
while game_on:
    D = Deck()
    D.shuffle_card()
    P1 = Player('Player1')
    D1 = Player('Dealer')
    P1.total_money()
    D1.total_money()
    P1.bet_money()
    P1.total_money()
    D1.money = P1.bet + D1.money
    D1.total_money()
    P1.add_card(D.deal_card())
    P1.add_card(D.deal_card())
    D1.add_card(D.deal_card())
    D1.add_card(D.deal_card())
    round_num = 1
    print(f"------!!!Round{round_num} Starts!!!-----")
    player_check()
    print(f"-----!!!Round{round_num} Ends!!!-----")
    play_on = 'null'
    while play_on != 'Y' and play_on != 'N':
        play_on = input('Enter Y(Yes)/No(N) to start/stop playing next round')
        continue
    else:
        if play_on == 'Y':
            continue
        if play_on == 'N':
            game_on = False
            break

print("-----GAME ENDS----")