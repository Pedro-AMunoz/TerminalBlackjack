# TerminalBlackjack

### Program Running Instructions
The program comes in 3 .py files, however only main.py needs to be run. The program can be run by typing `$
python main.py` in the command line, at which point the game immediately begins.
No additional dependencies besides a python interpreter are necessary, the
entire program uses no external libraries besides random.

Note: The Blackjack Brainstorm pdf is not necessary in understanding how the
program functions, it serves more as a collection of random and unorganized notes I
used in order to navigate the prompt. I figured it best to attach it with the other files as it
documents some of my thought process.

### Design Choices / Algorithmic Decisions
#### General Design Choices:
There are 4 driving forces in the game: (1) a player that takes inputs, (2) a
dealer with predefined behavior, (3) message displays, and (4) a main system
/ engine that enforces the ruleset of the game.
- Modularization in mind, the different utilities are divided into their
respective classes/methods: Player (encompassing the input player and
the dealer), Deck (offering any methods the deck may need), Display
(offering tools for displaying messages during the game), and the
WinLoseChecker() method (takes care of win/bust cases). These can all
be found in utils.py.
- The game itself can be found in main.py as a simple method call to
main(). Here, all utilities from the aforementioned file are referenced to
create the general flow of the game.

#### Players
- Players can be instantiated via the Player class, with a name fed in as an
argument.
- Players have 3 primary methods, along with a few helper methods that
are of no concern at the high-level. Players also have 5 attributes
(including the name attribute).

- Attributes:
1. self.name -> str. An identifier for who the player is, input-player or
dealer (helps the Display System differentiate between players).
2. self.hand -> List<str>. Stores/keeps track of all cards the player
has in their hand.
3. self.handSum -> int. Keeps track of the optimal overall sum of the
player’s hand.
4. self.numAces -> int. Indicates how many aces the player has in
their hand (helps in finding optimal sum).
5. self.prevAceVals -> int. Indicates the previous most optimal sum
of aces in the player’s hand (helps in finding optimal sum).

- Methods:
1. __init__(self, name: str) -> Player. Initializes a player.
2. hit(self, deck: Deck) -> None. Takes the argument deck and
draws a card from it, adding it to the player’s hand.
3. getHandValue(self) -> int. Returns the optimal sum of the player’s
hand in O(1) time.
4. Helper: addCard(self, card: str) -> None. Adds the given card to
the player’s hand. If the player has at least one Ace, check for a
new optimal value.
5. Helper: recalculateHandValue(self) -> None. Calculates the new
optimal hand sum in O(1) time by keeping track of the amount of
Aces as well as the Ace values prior to optimizing. There can be a
max of 1 Ace worth 11 points in a hand, meaning there are always
at most 2 options for Ace values: all 1s, or a single 11 and the rest
as 1s. By subtracting the previous Ace values from the current
hand sum, we can avoid re-summing the deck (excluding Aces).
Also by keeping track of the number of Aces, we can evaluate our
two options; self.numAces in the case of all 1s or (self.numAces -
1) + 11 in the case of a single 11. Summing this to (self.handSum -
self.prevAceVals) returns the new optimal hand value.

#### Cards
- The initial plan was to create a Card class that would specify attributes,
but I felt that was overcomplicating things for a project of this scope.
Representing cards as strings and accessing their respective values
from a str -> int map proved to be a simple yet efficient implementation.

#### The Deck
- The Deck class has 2 attributes and 4 methods, all fairly straightforward.
- Attributes:
1. self.deck -> List<str>. A collection of all 52 cards (4 of each type).
2. self.size -> int. Indicates how big the deck currently is. (Unused)
- Methods:
1. __init__(self) -> Deck. Initializes the deck and size.
2. shuffle(self) -> None. Uses the random library to randomize the
order of cards in self.deck.
3. draw(self) -> str. Picks and returns a card from self.deck by
popping the 0th element, ideally done AFTER the deck is shuffled
at least once (at the start of the game).
4. size(self) -> int. Returns the current size of the deck. (Unused)

#### Display System
- The Display System, which encompasses all visual feedback for the
game, is a class with 8 methods, one being a helper function. They are all
straightforward, being simple print statements that visualize what occurs in
the game.
- Methods:
- displayHand(self, player: Player, hiddenCards=0: int,
hideTotal=False: bool) -> None. Displays the hand of the given
player in the command line. The hiddenCards and hideTotal
arguments are optional, hiding no cards or the total by default, but
can hide the specified amount of cards/total by displaying them as
‘?’ in the command line.
- displayInputPromt(self) -> None. Displays the input options
during the input-player’s turn.
- displayHit(self, player: Player) -> None. Displays a message
stating the given player has hit.
- displayStandHand(self, player: Player) -> None. Displays a
message stating the given player has stood, along with their current
hand.
- displayWin(self, player: Player) -> None. Displays the given
player as the winner of the game, and their winning hand.
- displayBust(self, player: Player) -> None. Displays the given
player as the loser of the game, and their losing hand.
- displayTie(self) -> None. Displays a tie message.
- handToStr(self, player: Player) -> str. Converts the given player’s
hand into string format.

#### Rule Enforcer
- The rules are very simple for this game, all based on the value of their
hand:
1. If any player reaches 21, they automatically win.
2. If they go above 21 they automatically lose.
3. Any amount of points less than 21 means they are free to
Hit/Stand as desired.
- Given these three cases, I found it sufficient to create a method
WinLoseChecker(player: Player, display: Display) -> bool, which
checks what case the given player falls under and (if necessary)
communicates with the display to show the corresponding message in the
command line. If the case is game-ending (21 or bust), the method returns
true, otherwise false.

#### Game Structure
1. Phase 1:
The Display System and Deck are initialized along with both
Players (input and dealer), the Deck is shuffled. Players are then given 2
cards each from the Deck and their hands are displayed. There is a
case where a player gets (10/J/Q/K + Ace) as their starting hand, which is
21, thus we have a WinLose Check at the end of this phase.
2. Phase 2:
This is the input player’s turn. The player may Hit or Stand
whenever by entering H/h or S/s respectively in the command line. This
was implemented with a while(true) loop that checks for inputs. Any time
the player Hits, the updated hands are displayed and a WinLose Check
is done. When the player Stands, the while(true) loop breaks and the
dealer’s turn begins.
3. Phase 3:
This is the dealer’s turn. As predefined by the spec, the dealer will
Hit until their hand value is 17 or above. Every time the dealer Hits, the
updated hands are displayed and a WinLose Check is done.
4. Phase 4:
This is the final phase. If no player got 21 or above during their turn,
both scores are compared and the player with the highest score wins
(since it’s below 21), and their victory is displayed in the command line. In
the case of a tie, a tie message is displayed.

#### Ace optimality
- Refer to Design Choices / Algorithmic Decisions -> Players ->
Methods -> 5. .
