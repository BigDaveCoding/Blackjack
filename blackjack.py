import random

class Player:
    #creating a player class that will track various player variables. 
    #Will have various functions throughout that will control the flow of the game
    def __init__(self, name, money = 100, bet_amount = 0, cards = [], rounds_won = 0, rounds_lost = 0):
        self.name = name
        self.money = money
        self.bet_amount = bet_amount
        self.cards = cards
        self.rounds_won = rounds_won
        self.rounds_lost = rounds_lost
        
    def __repr__(self):
        return 'You have £{money} left. Your current hand is {cards}. Rounds won: {rounds_won}. Rounds Lost: {rounds_lost}'.format(money = self.money, cards = self.cards, rounds_won=self.rounds_won, rounds_lost = self.rounds_lost)

    def player_turn(self, turn):
        pass
    def player_win(self, amount):
        pass
    def player_lose(self, amount):
        pass
    

class Dealer:
    #Creating a dealer class which will be used to track the dealers cards.

    soft_17 = 17
    def __init__(self, cards, rounds_won, rounds_lost):
        self.cards = cards
        self.rounds_won = rounds_won
        self.rounds_lost = rounds_lost



class CardsInPlay:
    #this class will assign how many decks will be used throughout the game and keep track of which cards have been played and remove them from the deck gradually.

    cards_in_deck = {'Ace':4, 'Two':4, 'Three':4, 'Four':4, 'Five':4, 'Six':4, 'Seven':4, 'Eight':4, 'Nine':4, 'Ten':4, 'Jack':4, 'Queen':4, 'King':4}

    def __init__(self, decks, cards_played = {}):
        self.decks = decks
        self.card_amount = {key: value * decks for key, value in CardsInPlay.cards_in_deck.items()}
        self.cards_played = cards_played
            
    def __repr__(self):
        return 'There are {decks} decks in play. Here is each card and how many of each card there is: {dict}'.format(decks=self.decks, dict=self.card_amount)
    
class PlayRound:
    pass

player1 = Player('Dave', 100)
print(player1)
cards_in_play = CardsInPlay(random.randrange(1, 5))
print(cards_in_play)
