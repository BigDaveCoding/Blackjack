import random

class Player:
    #creating a player class that will track various player variables. 
    #Will have various functions throughout that will control the flow of the game
    player_total = 0
    dealer_total = 0
    values_of_cards = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}
    value_of_ace = [1, 11]

    def __init__(self, name, money = 100, bet_amount = 0, cards = None, card_total = 0, rounds_won = 0, rounds_lost = 0, is_dealer = False):
        self.name = name
        self.money = money
        self.bet_amount = bet_amount
        self.cards = cards or []
        self.card_total = card_total
        self.rounds_won = rounds_won
        self.rounds_lost = rounds_lost
        self.is_dealer = is_dealer

    def __repr__(self):
        return 'You have £{money} left. Rounds won: {rounds_won}. Rounds Lost: {rounds_lost}'.format(money = self.money, cards = self.cards, rounds_won=self.rounds_won, rounds_lost = self.rounds_lost)
    
    #this function uses a paameter called card which will be the class CardsInPlay.
    #Then calls upon a funtion within that class to return a random card. random card is the added to Player class card list.
    def deal_cards(self, card):
        self.cards.append(card.get_random_card())
        return "{name}'s cards: {cards}".format(name=self.name, cards=self.cards)
    
    def player_turn(self):
        turn_choices = ['hit', 'stand', 'double down', 'split']
        if self.cards[0] == self.cards[1]:
            player_choice = input('It\'s your turn: Hit / Stand / Double Down / Split : ')
        else:
            player_choice = input('It\'s your turn: Hit / Stand / Double Down : ')
        
        while player_choice.lower() not in turn_choices:
            player_choice = input('Please try again: ')
        if player_choice in turn_choices:
            print('You chose to {}'.format(player_choice))
        
        return player_choice
    
    
    def sum_cards(self, cards):
        self.card_total = 0
        for card in cards:
            for key, value in Player.values_of_cards.items():
                if card == key:
                    self.card_total += value
        if 'Ace' in cards:
            if self.card_total + Player.value_of_ace[1] <= 20:
                return 'You have an Ace, your total is either: {total_one} or {total_two}'.format(total_one = self.card_total + Player.value_of_ace[0], total_two = self.card_total + Player.value_of_ace[1])
            elif self.card_total + Player.value_of_ace[1] == 21:
                return 'You have 21!'
            else:
                return 'The total of your cards is {}'.format(self.card_total + Player.value_of_ace[0])
                 
        return 'The total of your cards is: {}'.format(self.card_total)

    def player_win(self, amount):
        pass
    def player_lose(self, amount):
        pass
    
class CardsInPlay:
    #this class will assign how many decks will be used throughout the game and keep track of which cards have been played and remove them from the deck gradually.

    cards_in_deck = {'Ace':4, 'Two':4, 'Three':4, 'Four':4, 'Five':4, 'Six':4, 'Seven':4, 'Eight':4, 'Nine':4, 'Ten':4, 'Jack':4, 'Queen':4, 'King':4}

    def __init__(self, decks, cards_played = {}):
        self.decks = decks
        self.card_amount = {key: value * decks for key, value in CardsInPlay.cards_in_deck.items()}
        self.cards_played = cards_played

    #this function adds cards to a list from the self.cards.amount dictionary if the value of that card is greater than 0.
    #then chooses a random card from the available cars list and decreases the dtionary key:value by 1.
    def get_random_card(self):
        available_cards = []
        for key, value in self.card_amount.items():
            if value > 0:
                available_cards.append(key)
               
        card = random.choice(available_cards)
        self.card_amount[card] -= 1
        return card
    
    def __repr__(self):
        return 'There are {decks} decks in play. Here is each card and how many of each card there is: {dict}'.format(decks=self.decks, dict=self.card_amount)
    

cards = CardsInPlay(random.randrange(1, 5))
dealer = Player('Dealer', 0, is_dealer = True)
player = Player('Dave')
#delaer gets first card
print(dealer.deal_cards(cards))
#player gets dealt two cards
player.deal_cards(cards)
print(player.deal_cards(cards))
#print sum of the two cards
print(player.sum_cards(player.cards))
#creating variable to store player choice
player_turn = player.player_turn()


if player_turn == 'hit':
    print(player.deal_cards(cards))
    print(player.sum_cards(player.cards))

if player.card_total == 21:
    pass

if player.card_total <= 20:
    pass
    
