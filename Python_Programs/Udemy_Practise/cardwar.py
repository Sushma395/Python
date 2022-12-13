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
round_num = 0

while game_on:
    round_num += 1
    print(f'Round Number: {round_num}')

    if len(player1.cards) == 0:
        print('player1 has 0 cards. player2 wins')
        game_on = False
        break
    if len(player2.cards) == 0:
        print('player2 has 0 cards. player1 wins')
        game_on = False
        break

    #game is one, new round has started
    player1_round = []
    player2_round = []
    player1_round.append(player1.remove_card())
    player2_round.append(player2.remove_card())

    round_on = True

    while round_on:
        if player1_round[-1].value > player2_round[-1].value:
            player1.add_cards(player2_round)
            player1.add_cards(player1_round)
            round_on = False

        elif player2_round[-1].value > player1_round[-1].value:
            player2.add_cards(player2_round)
            player2.add_cards(player1_round)
            round_on = False

        else:
            print('At WAR')
            #equal cards
            if len(player1.cards) < 5:
                print('player1 has less cards. player2 wins')
                game_on = False
                break
            elif len(player2.cards) < 5:
                print('player2 has less cards. player1 wins')
                game_on = False
                break
            else:
                for i in range(5):
                    player1_round.append(player1.remove_card())
                    player2_round.append(player2.remove_card())
                print('5 cards added to each player')

    print(f'len of P1: {len(player1.cards)}')
    print(f'len of P2: {len(player2.cards)}')


