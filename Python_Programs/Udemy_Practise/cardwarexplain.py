import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'suit {self.suit} has rank {self.rank} and value {self.value}'


class Deck:
    def __init__(self,):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def remove_card(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return self.all_cards


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_card(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.cards)} cards'


# new game
new_deck = Deck()
new_deck.shuffle()

player1 = Player('P1')
player2 = Player('P2')

game_on = True
for i in range(26):
    player1.add_cards(new_deck.remove_card())
    player2.add_cards(new_deck.remove_card())

while game_on:

    if len(player1.cards) == 0:
        print('player1 has 0 cards. player2 wins')
        game_on = False
        break
    if len(player2.cards) == 0:
        print('player2 has 0 cards. player1 wins')
        game_on = False
        break
    round_num = 0
    war_on = True

    while war_on:
        player1_round = []
        player2_round = []
        round_num += 1
        print(f'Round_Number: {round_num}')
            #game is one, new round has started
        print(f'P1 before:{len(player1.cards)}')
        print(f'P2 before:{len(player2.cards)}')
        player1_round.append(player1.remove_card())
        player2_round.append(player2.remove_card())
        print(f'P1 card:{player1_round[-1]}')
        print(f'P2 card:{player2_round[-1]}')


        if player1_round[-1].value > player2_round[-1].value:
            player1.add_cards(player2_round)
            player1.add_cards(player1_round)

        elif player2_round[-1].value > player1_round[-1].value:
            player2.add_cards(player2_round)
            player2.add_cards(player1_round)

        else:
            print('At WAR. Same value')
            #equal cards

        if round_num > 5:
            game_on = False
            war_on = False
            break

        print(f'P1 after:{len(player1.cards)}')
        print(f'P2 after:{len(player2.cards)}')



