from utils import *

##PLAYER TESTING START##
def playerFunctionalityTests():
    playerTestSimple()
    print("\n")
    playerTestSingleAce()
    print("\n")
    playerTestMultipleAces()
    print("\n")
    playerTestAllAces()
    print("\n")

def playerTestSimple():
    player = Player("p")
    print(player.getHandValue()) #0
    player.addCard("7")
    print(player.getHandValue()) #7
    player.addCard("K")
    print(player.getHandValue()) #17

def playerTestSingleAce():
    player = Player("p")
    player.addCard("A")
    print(player.getHandValue()) #11
    player.addCard("9")
    print(player.getHandValue()) #20
    player.addCard("2")
    print(player.getHandValue()) #12
    
def playerTestMultipleAces():
    player = Player("p")
    player.addCard("A")
    player.addCard("A")
    print(player.getHandValue()) #12
    player.addCard("5")
    print(player.getHandValue()) #17
    player.addCard("A")
    print(player.getHandValue()) #18

def playerTestAllAces():
    player = Player("p")
    player.addCard("A")
    print(player.getHandValue()) #11
    player.addCard("A")
    print(player.getHandValue()) #12
    player.addCard("A")
    print(player.getHandValue()) #13
    player.addCard("A")
    print(player.getHandValue()) #14
    player.addCard("10")
    print(player.getHandValue()) #14
    player.addCard("10")
    print(player.getHandValue()) #24
##PLAYER TESTING END##

##DECK TESTING START##
def deckFunctionalityTests(n):
    deckTestSimple()
    deckTestShuffle(n)
    deckTestDraw(n)

def deckTestSimple():
    deck = Deck()
    print("Deck size: " + str(deck.size))
    print(*deck.deck)

def deckTestShuffle(n):
    deck = Deck()
    for i in range(n):
        deck.shuffle()

        print("**Iteration " + str(i) + " shuffle**")
        print(*deck.deck)
        print("\n")

def deckTestDraw(n):
    deck = Deck()
    deck.shuffle()
    print("Deck size: " + str(deck.size))

    draws = []
    for i in range(n):
        draws.append(deck.draw())

        print("\nPlayer draws: ")
        print(*draws)
        print("\n")
        print("Deck Size: " + str(deck.size) + ", Deck :")
        print(*deck.deck)
##DECK TESTING END##

##HIT/BUST TESTING START##
def hitTest(n):
    deck = Deck()
    deck.shuffle()

    player = Player("p")

    display = Display()

    for i in range(n):
        print(player.hit(deck))
        WinLoseChecker(player, display)
    print("Total value: " + str(player.getHandValue()))
##HIT/BUST TESTING END##


##DISPLAY TESTING START##
def displayHandTest(draws, hiddenCards):
    display = Display()
    player = Player("p")
    deck = Deck()
    deck.shuffle()

    for i in range(draws):
        player.hit(deck)

    display.displayHand(player, hiddenCards=hiddenCards)
##

def allTests(n):
    print("-- PLAYER TESTS --")
    playerFunctionalityTests()
    print("\n\n")

    print("-- DECK TESTS --")
    deckFunctionalityTests(n)
    print("\n\n")

    print("-- HIT/BUST TESTS --")
    hitTest(n)
    print("\n\n")

    print("-- DISPLAY TESTS --")
    displayHandTest(3, 1)
    print("\n\n")

allTests(3)
