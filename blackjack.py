import random

class Player:
    #creating a player class that will track various player variables. 
    #Will have various functions throughout that will control the flow of the game
    player_total = 0
    dealer_total = 0
    values_of_cards = {'Ace': 11, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}
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
            player_choice = input('It\'s your turn: Hit or Stand? : ')
        else:
            player_choice = input('It\'s your turn: Hit or Stand? : ')
        
        while player_choice.lower() not in turn_choices:
            player_choice = input('Please try again: ')
        if player_choice in turn_choices:
            print('You chose to {}'.format(player_choice))
        
        return player_choice
    
    def has_ace(self, cards):
        total_one = 0
        total_two = 0

        # for card in cards:
        #     if card != 'Ace':
        #         return
            
        for card in cards:
            if card == 'Ace':
                total_one +=1
                total_two += 11
            for key, value in Player.values_of_cards.items():
                if card == key and key != 'Ace':
                    total_one += value
                    total_two += value
    
        if total_one < 21 and total_two < 21:
            return 'Sum of your cards is either: {one} or {two}'.format(one = total_one, two = total_two)
        if total_one < 21:
            return 'Card total is {}'.format(total_one)
        if total_two < 21:
            return 'Card total is {}'.format(total_two)
    
    
    def sum_cards(self, cards):
        self.card_total = 0
        for card in cards:
            for key, value in Player.values_of_cards.items():
                if card == key:
                    self.card_total += value         
        return 'The total of {name}\'s cards is: {total}'.format(name = self.name, total = self.card_total)
    
    def double_down(self, current_hand, cardsinplay):
        hand_one = [current_hand[0]]
        hand_two = [current_hand[1]]
        return 'First hand: {hand_one}\nSecond hand: {hand_two}'.format(hand_one=hand_one, hand_two=hand_two)
    
    def who_wins(self, dealer, amount):
        if dealer.card_total > 21:
            self.money += amount
            return 'You Win! You won £{}'.format(amount * 2)
        if self.card_total == dealer.card_total:
            return 'It\'s a tie! '
        if self.card_total > dealer.card_total:
            self.money += amount
            return 'You Win! You won £{}.'.format(amount * 2)
        if self.card_total < dealer.card_total:
            self.money -= amount
            return 'You Lose! :( You lost £{}.'.format(amount)
        
    def play_again(self):
        self.cards = []
        self.card_total = 0


    def player_win(self, amount):
        pass
    def player_lose(self, amount):
        pass
    def tie(self, amount):
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

def play_again(player, dealer):
    while True:
        again = input('Do you want to play again? (yes/no): ').lower()
        if again == 'yes':
            player.play_again()
            dealer.play_again()
            return True
        elif again == 'no':
            return False
        else:
            print('Invalid input. Please enter either "yes" or "no".')

cards = CardsInPlay(random.randrange(1, 5))
dealer = Player('Dealer', 0, is_dealer = True)
player = Player('Dave')

player_lost = False
player_has_ace = False

while True:
    #Player places bet
    while True:
        try:
            bet_amount = int(input('You have £{money}. How much would you like to bet? £'.format(money=player.money)))
            if bet_amount <= player.money:
                break  # exit the loop if the conversion is successful
            else: 
                print('You don\'t have that much money :(')
        except ValueError:
            print("Invalid input.")
    #dealer gets first card
    print(dealer.deal_cards(cards))
    #player gets dealt two cards
    # player.deal_cards(cards)
    player.cards.append('Ace')
    print(player.deal_cards(cards))


    #print sum of the two cards
    # print(player.sum_cards(player.cards))

    if 'Ace' in player.cards:
        player_has_ace = True
        player.has_ace(player.cards)
        print('you have an ace')
    else:
        print(player.sum_cards(player.cards))

    if player_has_ace:
        print(player.has_ace(player.cards))
    else:
        #Will loop whilst the players card total is less than 21 or they choose to stand.
        while player.card_total < 21:
            player_turn = player.player_turn()
            if player.card_total == 21:
                print('You have 21')
                break
            if player_turn == 'hit':
                print(player.deal_cards(cards))
                print(player.sum_cards(player.cards))
            if player_turn == 'stand':
                break

    if player.card_total == 21:
        print('You have 21! Let\'s see what the dealer draws')


    if player.card_total > 21:
        player_lost = True

    if player_lost is not True:
        print(dealer.deal_cards(cards))
        print(dealer.sum_cards(dealer.cards))

        while dealer.card_total < 17:
            print(dealer.deal_cards(cards))
            print(dealer.sum_cards(dealer.cards))
        if dealer.card_total >= 17:
            print(player.who_wins(dealer, bet_amount))
        
    else:
        print('Better luck next time')

    if not play_again(player, dealer):
        print('Thanks for playing!')
        break


    
