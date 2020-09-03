import random
suit=('Hearts','Diamonds','Spades','Clubs') #Creates a tuple of different suits-global
rank=('Two','Three','Four','Five','Six' ,'Seven' ,'Eight', 'Nine' , 'Ten' ,'Jack', 'Queen' ,'King' ,'Ace')#creates a tuple of their rank- global
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6 ,'Seven':7 ,'Eight':8, 'Nine':9, 'Ten':10 ,'Jack':10, 'Queen':10 ,'King':10 ,'Ace':11}#creates a dictionary to link values to their rank-global
playing=True#control variable for the game

class Card():
    def __init__(self,suit,rank): # initialises the variables for the class will use the global suit and rank
        self.suit=suit # class using suit
        self.rank=rank # class using rank

    def __str__(self):

        return self.rank +  ' Of ' + self.suit # returns a string version of the suit and rank together in a sentence but it cant be implemented yet as it is a tuple + a string + a tuple

class Deck():
    def __init__(self,suit,rank):# initialises the variables for the class will use the global suit and rank
        self.deck=[] #creates a array called deck
        for i in rank: # for loop for each value in rank
            for j in suit:# for loop for each value in suit
                self.deck.append(Card(j,i))#this puts single values of suit and rank FROM CARD into the deck array and so deck will hold 52 instances of Card class
                #this means only deck can access variables from the card class
  

    def __str__(self):
        display_deck=''#use this as a variable to add the other strings to
        for deck in self.deck:
            display_deck+='\n'+deck.__str__()#because rank and suit have been made singl values they can be printed and added as strings in the format in CARD class
        return display_deck

    def shuffle(self):

        random.shuffle(self.deck)#shuffles the deck

    def deal(self):
        deal_card=self.deck.pop()#this methed takes out a cell in the array 
        return deal_card
                
class Hand():
    def __init__(self):
        self.player_deck=[] #creates an empty array for the players deck
        self.value=0 #Value will start at zero will be used later to add value of card
        self.ace=False #whether an ace is present or not



    def add_card(self,card):
        self.player_deck.append(card) #will uses the card that is dealt and put it into an array for the player deck
        self.value+= value[card.rank] # uses the dictionary to add the value of that card to self value
        if 'A' in card.rank: # checks whether it is an ace or not
            self.ace=True

    def __str__(self):

        display_deck=''
        for deck in self.player_deck:
            display_deck+= deck.__str__() + ', '


        return display_deck



    


    def auto_adjust_for_ace(self,card):
        if self.value >21 and self.ace: # if the total is more than 21 and an ace is present it will adjust it to make it a one
            self.value-=10
            self.ace=False #ace is reset to false

        return

class Chips():
    def __init__(self):#player_total is a parameter that will be passed to the class
        self.total=0
        self.bet=0#bet is set to zero
        

    def set_bank(self,i):
        self.total=int(input(f'Player {i}\nHow much do you have in the bank: '))
        

    def make_bet(self):
        valid_bet=0
        while not valid_bet:
            self.bet=int(input('How much would you like to bet: '))
            if self.bet > self.total:
                print('You do not have enough in your bank \nPlease enter a new amount')
               

            else:
                valid_bet=1
            print()



    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

def print_deck(num_of_players):#
    for i in range(1,num_of_players):
        print()
        print(f'Player {i} these are your starting cards: ')
        print(hand[i])
        print(f'Total value is: {hand[i].value}')
        print()

    print('These are the dealers starting cards: ')
    print(hand[0])
    print(f'Total value is: {hand[0].value}')
    print()

def player_move(hand,i):
    hit=1
    while hit:
        move=int(input(f'Player {i} would you like to\n1)Hit\n2)Stand\nChoose 1 or 2 :'))
        if move ==1:
            dealt_card=deck.deal()
            hand.add_card(dealt_card)
            hand.auto_adjust_for_ace(dealt_card)
            print('Hit!')
            print(hand)
            print(f'Total value of hand is: {hand.value}')
        else:
            print('Stand')
            print(hand)
            hit=0

        print()

    return hand.value



num_of_players=int(input('How many players: '))
num_of_players+=1
deck= Deck(suit,rank)
deck.shuffle()
hand=[Hand() for each in range(num_of_players)]
chips=[Chips() for each in range(num_of_players)]

for i in range(num_of_players):
    for j in range(2):
        dealt_card=deck.deal()
        hand[i].add_card(dealt_card)
        hand[i].auto_adjust_for_ace(dealt_card)

for i in range(1,num_of_players):
    chips[i].set_bank(i)
    chips[i].make_bet()

print_deck(num_of_players)


for i in range(1,num_of_players):
    player_move(hand[i],i)


print()


for i in range(1,num_of_players):
    
    if hand[0].value > hand[i].value and hand[0].value <=21 or hand[i].value > 21:
        
        chips[i].lose_bet()
        print('BUST')
        print(f'Player {i} loses ${chips[i].bet}')
        print(f'Player {i} has ${chips[i].total}')
        print()
    elif hand[0].value==21 and hand[i].value ==21:
        print('DRAW')
        print(f'Player {i} has ${chips[i].total}')
        print()

    else:
        chips[i].win_bet()
        print('WIN!')
        print(f'Player {i} wins ${chips[i].bet}')
        print(f'Player {i} has ${chips[i].total}')
        print()

    

        

   










   

        
      
      



        