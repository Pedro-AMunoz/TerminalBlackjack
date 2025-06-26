import random

cards = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.handSum = 0

        self.numAces = 0
        self.prevAceVals = 0 #Helps not have to recalculate sum of non-ace cards in the hand, more efficient
 
    def hit(self, deck):
        card = deck.draw()
        self.addCard(card)
        return card

    def getHandValue(self):
        return self.handSum
    
                    ##HELPER FUNCTIONS##

    #If any Ace is in the hand, calculate new optimal hand value
    def addCard(self, card):
        self.hand.append(card)
        if (card == "A"):
            self.numAces += 1
        else:
            self.handSum += cards[card]
 
        if self.numAces > 0:
            self.recalculateHandValue()
 
    #Finds optimal Ace values
    def recalculateHandValue(self):
        handVal = self.handSum - self.prevAceVals
        
        allOnes = self.numAces 
        oneEleven = (self.numAces - 1) + 11

        if handVal + oneEleven <= 21:
            self.handSum = handVal + oneEleven
            self.prevAceVals = oneEleven
        else:
            self.handSum = handVal + allOnes
            self.prevAceVals = allOnes
        return


class Deck:
    def __init__(self):
        self.deck = []
        for card in cards.keys():
            for i in range(4):
                self.deck.append(card)
        
        self.size = 52

    #Randomizes the order of the deck
    def shuffle(self):
        random.shuffle(self.deck)
        return
    
    #Draws a card from the deck (pop 0th element for efficiency)
    def draw(self):
        self.size -= 1
        return self.deck.pop(0)

    def size(self):
        return self.size


class Display:
    #Hide args tell display how many cards to hide by replacing their string representation with ? in the print
    def displayHand(self, player, hiddenCards=0, hideTotal=False):
        if hiddenCards > len(player.hand):
            raise Exception("Too many hidden cards!")

        playerIdentifier = player.name + " has: "

        handStr = ""
        for i in range(len(player.hand)):
            if hiddenCards > 0:
                handStr += "? "
                hiddenCards -= 1
            else:
                handStr += player.hand[i] + " "

        if hideTotal:
            print(playerIdentifier + handStr + " = ?")
        else:
            print(playerIdentifier + handStr + " = " + str(player.getHandValue()))

    def displayInputPrompt(self):
        print("\nWould you like to (H)it or (S)tand?")

    def displayHit(self, player):
        print("\n" + player.name + " hits!")

    def displayStandHand(self, player):
        print("\n" + player.name +  " stands with: " + self.handToStr(player) + " = " + str(player.getHandValue()))

    def displayWin(self, player):
        print("\n" + player.name + " wins with: " + self.handToStr(player) + " = " + str(player.getHandValue()) + "!")

    def displayBust(self, player):
        print("\n" + player.name + " busts with " + str(player.getHandValue()) + "!")

    def displayTie(self):
        print("\nPlayers tie!")

                ## HELPER FUNCTIONS ##
    
    def handToStr(self, player):
        handStr = ""
        for i in range(len(player.hand)):
            handStr += " " + player.hand[i]
        return handStr


#Will be responsible for sending a win/loss/continue message to the game system for desired behavior, returns true if game should end, otherwise false
def WinLoseChecker(player, display):
    handSum = player.getHandValue()
    
    if handSum > 21:
        #Bust
        display.displayBust(player)
        return True
    elif handSum == 21:
        #Win
        display.displayWin(player)
        return True
    else:
        return False
