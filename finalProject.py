'''
Everyone has their favorite card game. What's yours? For this assignment, choose a card game (other than Blackjack), 
and turn it into a Python program. It doesn't matter if it's a 1-player game, or a 2 player game, or more! 
That's totally up to you. A few requirements:

It's got to be a card game (no board games, etc)
When the game starts up, you should ask for the players' names. And after they enter their names, your game should 
refer to them by name only. ("It's John's turn" instead of "It's player 1's turn). 
At any point during the game, someone should be able to type "--help" to be taken to a screen where they can read the 
rules of the game and instructions for how to play. After they're done reading, they should be able to type "--resume" 
to go back to the game and pick up where they left off.



Extra Credit:

Want to make this much much harder on yourself? Okay, you asked for it!

For extra credit, allow 2 players to play on two different computers that are on the same network. Two people should be 
able to start identical versions of your program, and enter the internal IP address of the user on the network who they 
want to play against. The two applications should communicate with each other, across the network using simple HTTP requests. 
Try this library to send requests:

http://docs.python-requests.org/en/master/
http://docs.python-requests.org/en/master/user/quickstart/

And try Flask to receive them:

http://flask.pocoo.org/

The 2-player game should only start if one person has challenged the other (by entering their internal IP address), and the 2nd 
person has accepted the challenge. The exact flow of the challenge mechanism is up to you.


thirty-one? https://playingcarddecks.com/blogs/how-to-play/thirty-one-game-rules



Card Game Rules
Thirty One, is a casino type card game for 2 or more people and is played with a standard 52 playing card deck. In Thirty One, 
Aces are worth 11 points, face cards are worth 10 points and numbered cards are worth their pip value. The objective of the game is to have a hand 
equal to or as close to 31 as possible.

Set Up
The deck is shuffled and 3 cards are dealt to each player. The remaining deck forms the stock and then a card is flipped over to form a 
discard pile. 

How to Play
Player 1 begins gameplay. When it is their turn, players choose to either pick a card from the stock or from the discard pile 
and then they must discard one of their cards, all in an attempt to get a hand as close or equal to 31.

Only cards of the same suit count as points. For example, if a player has an Aces of Spades, an 8 of Spades, and a King of Hearts, the player’s hand is 
worth 19.

When a player is comfortable with their hand, they knock on the table. All other players then have one more draw to try and improve their hand. 
The player with the lowest hand loses for that round. Each player starts with 4 points and whoever loses all their points first, loses.
If the player who knocks has the lowest hand, they give up 2 points rather than 1. When a player loses 4 times, they are out of the game. 
The last player standing wins the game.  

'''

from random import shuffle
from itertools import groupby
import numpy as np

global deck, x, y, suit, highSuit, discardPile, player, player1, player2, stringPlayer
def createDeck():
    global deck, x, y, suit
    deck = []
    faceValues = ["A","K","Q","J"]
    suit = [" Hearts"," Spades"," Diamonds"," Clubs"]
    x  = 0
    y = 0

    for c in range(4):
        for card in range (2,11):
            deck.append(str(card) + str(suit[x]))
        x+=1
    x = 0
    for c in range(4):
        for card in faceValues:
            deck.append(str(faceValues[y]) + str(suit[x]))
            y += 1
        x += 1
        y = 0

    shuffle(deck)
    return deck

#Create and shuffle deck and deal first hand.
createDeck()
player1Hand = [str(deck.pop()), str(deck.pop()), str(deck.pop())]
player2Hand = [str(deck.pop()), str(deck.pop()), str(deck.pop())]
discardPile = str(deck.pop())



class Player:
    def __init__(self, hand = [], points = 4):
        self.hand = hand
        self.points = points
        self.score = self.setScore()

    def __str__(self): #allows us to call print(Player)
        currentHand = "" #self.hand = ["A", "10"] -> "A 10"
        for card in self.hand:
            currentHand += str(card) + " "

        finalStatus = currentHand + "score: " + str(self.score)
        return finalStatus

    def playerSwitch(self):
        if player1.points == 0:
            print("Player 2 wins! Great game everyone! ")
            exit()
        elif player2.points == 0:
            print("Player 1 wins! Great game everyone! ")
            exit()
        elif player == player1:
            player = player2
            player2.newTurn()
        elif player == player2:
            player = player1
            player1.newTurn()


        
        return player

    def setScore(self):
        # Tallies the number of points per suit
        self.score = 0

        faceCardDict = {"A":11,"K":10,"Q":10,"J":10,"10":10,"9":9,"8":8,"7":7,
                        "6":6,"5":5,"4":4,"3":3,"2":2}
        suitScore = { "Hearts":0, "Diamonds":0, "Spades":0, "Clubs":0 }

        for card in self.hand:
            if "Hearts" in card:
                suitScore["Hearts"] += faceCardDict[card.split(" ")[0]]

            elif "Diamonds" in card:
                suitScore["Diamonds"] += faceCardDict[card.split(" ")[0]]

            elif "Spades" in card:
                suitScore["Spades"] += faceCardDict[card.split(" ")[0]]

            elif "Clubs" in card:
                suitScore["Clubs"] += faceCardDict[card.split(" ")[0]]

            highSuit = max(suitScore, key=suitScore.get)
            self.score = suitScore[highSuit] # highest total for a single suit = player's score

        return self.score 
    
    def pointLoss(self):
        self.points -= 1
        return self.points

    def newTurn(self):
        global discardPile, player, player1, player2, stringPlayer

        print("\nIt is player " + str(stringPlayer) + "'s turn.")
        print("Your current hand is " + str(self.hand) + " \nYour current score is " + str(self.score))
        print("\nThe card on the discard pile is the " + str(discardPile) + ".")
        playerChoice = input("Would you like to pick a card off the deck or the discard pile? (Type Deck or Discard) ")
        while playerChoice == "Deck" or playerChoice == "Discard":
            if playerChoice == "Deck":
                self.hand.append(str(deck.pop()))
                print("\nThe card from the deck has been added to your hand.\n" + str(self.hand))
                while (True):
                    discard = str(input("\nWhich card do you want to discard? Please type it in exactly how it appears on the screen. "))
                    if discard in self.hand:
                        self.hand.remove(discard)
                        discardPile = discard
                        self.setScore()
                        print("\nYour new hand is: " + str(self.hand))
                        print("Your new score is " + str(self.score))
                        knock = input("Do you want to knock? (Y/N)")
                        while knock == "Y" or knock =="N":
                            if knock == "N":
                                if player == player1:
                                    player = player2
                                    stringPlayer = "2"
                                    player2.newTurn()  
                                if player == player2:
                                    player = player1
                                    stringPlayer = "1"
                                    player1.newTurn() 
                            elif knock == "Y":
                                if player == player1:
                                    player = player2
                                    stringPlayer = "Player 2"
                                    print("\nIt is player " + str(stringPlayer) + "'s turn.")
                                    print("Your current hand is " + str(player2.hand) + " \nYour current score is " + str(player2.score))
                                    print("\nThe card on the discard pile is the " + str(discardPile) + ".")
                                    playerChoice = input("This is your last turn. Would you like to pick a card off the deck or the discard pile? (Type Deck or Discard) ")  
                                    if playerChoice ==  "Deck":
                                        player2.hand.append(str(deck.pop()))
                                    elif playerChoice == "Discard":
                                        player2.hand.append(str(discardPile))
                                    while (True):
                                        print("\nYour new hand is: " + str(player2.hand))
                                        print("Your new score is " + str(player2.score))
                                        discard = str(input("\nWhich card do you want to discard? Please type it in exactly how it appears on the screen. "))
                                        if discard in player2.hand:
                                            player2.hand.remove(discard)
                                            discardPile = discard
                                            player2.setScore()
                                            print("\nYour new hand is: " + str(player2.hand))
                                            print("Your new score is " + str(player2.score))
                                            if player1.score > player2.score:
                                                print("Player 1 is the winner of that round.")
                                                player2.pointLoss()
                                                if player2.points == 0:
                                                    print("Player 1 is the winner! Thanks for playing!")
                                                    exit()
                                            elif player2.score > player1.score:
                                                print("Player 2 is the winner of that round.")
                                                player1.pointLoss()
                                                if player1.points == 0:
                                                    print("Player 2 is the winner! Thanks for playing!")
                                                    exit()
                                            print("Player 1 has " + str(player1.score) + " points and player 2 has " + str(player2.score) + " points.")
                                        else:
                                            print("\nPlease re-enter the card again. You made a mistake. ")
                                if player == player2:
                                    player = player1
                                    stringPlayer = "Player 1"
                                    print("\nIt is player " + str(stringPlayer) + "'s turn.")
                                    print("Your current hand is " + str(player1.hand) + " \nYour current score is " + str(player1.score))
                                    print("\nThe card on the discard pile is the " + str(discardPile) + ".")
                                    playerChoice = input("This is your last turn. Would you like to pick a card off the deck or the discard pile? (Type Deck or Discard) ")  
                                    if playerChoice ==  "Deck":
                                        player1.hand.append(str(deck.pop()))
                                    elif playerChoice == "Discard":
                                        player1.hand.append(str(discardPile))
                                    while (True):
                                        print("\nYour new hand is: " + str(player1.hand))
                                        print("Your new score is " + str(player1.score))
                                        discard = str(input("\nWhich card do you want to discard? Please type it in exactly how it appears on the screen. "))
                                        if discard in player1.hand:
                                            player1.hand.remove(discard)
                                            discardPile = discard
                                            player1.setScore()
                                            print("\nYour new hand is: " + str(player1.hand))
                                            print("Your new score is " + str(player1.score))
                                            if player1.score > player2.score:
                                                print("Player 1 is the winner of that round.")
                                                player2.pointLoss()
                                                if player1.points == 31:
                                                    player2.pointLoss
                                                if player2.points == 0:
                                                    print("Player 1 is the winner! Thanks for playing!")
                                                    exit()
                                            elif player2.score > player1.score:
                                                print("Player 2 is the winner of that round.")
                                                player1.pointLoss()
                                                if player2.points == 31:
                                                    player1.pointLoss
                                                if player1.points == 0:
                                                    print("Player 2 is the winner! Thanks for playing!")
                                                    exit()
                                            print("Player 1 has " + str(player1.score) + " points and player 2 has " + str(player2.score) + " points.")
                                        else:
                                            print("\nPlease re-enter the card again. You made a mistake. ")
                            else:
                                print("Please enter either Y or N.")
                    else:
                        print("\nPlease re-enter the card again. You made a mistake. ")
            elif playerChoice == "Discard":
                self.hand.append(str(discardPile))
                print("\nThe card from the discard pile has been added to your hand.\n" + str(self.hand))
                while (True):
                    discard = str(input("\nWhich card do you want to discard? Please type it in exactly how it appears on the screen. "))
                    if discard in self.hand:
                        self.hand.remove(discard)
                        discardPile = discard
                        self.setScore()
                        print("\nYour new hand is: " + str(self.hand))
                        print("Your new score is " + str(self.score))
                        knock = input("Do you want to knock? (Y/N)")
                        while knock == "Y" or knock =="N":
                            if knock == "N":
                                if player == player1:
                                    player = player2
                                    stringPlayer = "2"
                                    player2.newTurn()  
                                if player == player2:
                                    player = player1
                                    stringPlayer = "1"
                                    player1.newTurn() 
                            elif knock == "Y":
                                if player == player1:
                                    player = player2
                                    stringPlayer = "Player 2"
                                    print("\nIt is player " + str(stringPlayer) + "'s turn.")
                                    print("Your current hand is " + str(player2.hand) + " \nYour current score is " + str(player2.score))
                                    print("\nThe card on the discard pile is the " + str(discardPile) + ".")
                                    playerChoice = input("This is your last turn. Would you like to pick a card off the deck or the discard pile? (Type Deck or Discard) ")  
                                    if playerChoice ==  "Deck":
                                        player2.hand.append(str(deck.pop()))
                                    elif playerChoice == "Discard":
                                        player2.hand.append(str(discardPile))
                                    while (True):
                                        print("\nYour new hand is: " + str(player2.hand))
                                        print("Your new score is " + str(player2.score))
                                        discard = str(input("\nWhich card do you want to discard? Please type it in exactly how it appears on the screen. "))
                                        if discard in player2.hand:
                                            player2.hand.remove(discard)
                                            discardPile = discard
                                            player2.setScore()
                                            print("\nYour new hand is: " + str(player2.hand))
                                            print("Your new score is " + str(player2.score))
                                            if player1.score > player2.score:
                                                print("Player 1 is the winner of that round.")
                                                player2.pointLoss()
                                                if player2.points == 0:
                                                    print("Player 1 is the winner! Thanks for playing!")
                                                    exit()
                                            elif player2.score > player1.score:
                                                print("Player 2 is the winner of that round.")
                                                player1.pointLoss()
                                                if player1.points == 0:
                                                    print("Player 2 is the winner! Thanks for playing!")
                                                    exit()
                                            print("Player 1 has " + str(player1.points) + " points and player 2 has " + str(player2.points) + " points.")
                                        else:
                                            print("\nPlease re-enter the card again. You made a mistake. ")
                                if player == player2:
                                    player = player1
                                    stringPlayer = "Player 1"
                                    print("\nIt is player " + str(stringPlayer) + "'s turn.")
                                    print("Your current hand is " + str(player1.hand) + " \nYour current score is " + str(player1.score))
                                    print("\nThe card on the discard pile is the " + str(discardPile) + ".")
                                    playerChoice = input("This is your last turn. Would you like to pick a card off the deck or the discard pile? (Type Deck or Discard) ")  
                                    if playerChoice ==  "Deck":
                                        player1.hand.append(str(deck.pop()))
                                    elif playerChoice == "Discard":
                                        player1.hand.append(str(discardPile))
                                    while (True):
                                        print("\nYour new hand is: " + str(player1.hand))
                                        print("Your new score is " + str(player1.score))
                                        discard = str(input("\nWhich card do you want to discard? Please type it in exactly how it appears on the screen. "))
                                        if discard in player1.hand:
                                            player1.hand.remove(discard)
                                            discardPile = discard
                                            player1.setScore()
                                            print("\nYour new hand is: " + str(player1.hand))
                                            print("Your new score is " + str(player1.score))
                                            if player1.score > player2.score:
                                                print("Player 1 is the winner of that round.")
                                                player2.pointLoss()
                                                if player2.points == 0:
                                                    print("Player 1 is the winner! Thanks for playing!")
                                                    exit()
                                            elif player2.score > player1.score:
                                                print("Player 2 is the winner of that round.")
                                                player1.pointLoss()
                                                if player1.points == 0:
                                                    print("Player 2 is the winner! Thanks for playing!")
                                                    exit()
                                            print("Player 1 has " + str(player1.points) + " points and player 2 has " + str(player2.points) + " points.")
                                        else:
                                            print("\nPlease re-enter the card again. You made a mistake. ")
                            else:
                                print("Please enter either Y or N.")
                    else:
                        print("\nPlease re-enter the card again. You made a mistake. ")
            else:
                print("\nPlease enter either Deck or Discard.")
        return self.hand

#Create 2 players and assign the starting turn
player1 = Player(player1Hand)
player2 = Player(player2Hand)  
player = player1
stringPlayer = "1"
player1.newTurn()

print(player1.score)
print(player2.score)


