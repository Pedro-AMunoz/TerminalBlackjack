from utils import *

#Game
def main():
    ##PHASE 1: Start##
    #Init
    display = Display()
    deck = Deck()
    deck.shuffle()
    player = Player("Player")
    dealer = Player("Dealer")
    #Starting deal
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    #Display hands
    display.displayHand(dealer, hiddenCards=1, hideTotal=True)
    display.displayHand(player)
    #Case K and A starting hand end check
    pEnd = WinLoseChecker(player, display)
    dEnd = WinLoseChecker(dealer, display)
    if pEnd or dEnd:
        if pEnd and dEnd:
            display.displayTie()
        return


    ##PHASE 2: Player's Turn##
    display.displayInputPrompt()
    while (True):
        key = input()
        
        #Hit
        if key.upper() == "H":
            player.hit(deck)

            display.displayHand(dealer, hiddenCards=1, hideTotal=True)
            display.displayHand(player)

            end = WinLoseChecker(player, display)
            if end:
                return
            
            display.displayInputPrompt()

        #Stand
        elif key.upper() == "S":
            display.displayStandHand(player)
            break
    

    ##PHASE 3: Dealer's Turn##
    while(dealer.getHandValue() < 17):
        dealer.hit(deck)
        display.displayHit(dealer)
        
        display.displayHand(dealer, hiddenCards=1, hideTotal=True)
        display.displayHand(player)

        end = WinLoseChecker(dealer, display)
        if end:
            return
    display.displayStandHand(dealer)


    ##PHASE 4: End##
    display.displayHand(dealer)
    display.displayHand(player)

    if player.getHandValue() > dealer.getHandValue():
        display.displayWin(player)
    elif player.getHandValue() < dealer.getHandValue():
        display.displayWin(dealer)
    else: 
        display.displayTie()

    return 

main()