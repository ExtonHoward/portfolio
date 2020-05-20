from random import shuffle

class Deck:
    #Creates card objects for all cards in standard deck
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Card:
    suits = ["Spades","Hearts","Diamonds","Clubs"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        # suits & values are integers
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        return False

    def __eq__(self, c2):
        if self.value == c2.value:
            return True
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("Player 1 name: ").title()
        name2 = input("Player 2 name: ").title()
        tie = "It's a tie. Neither player"
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.tie = Player(tie)

    def wins(self, winner):
        w = "{} wins this round.\n"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}, {} drew {}."
        d = d.format (p1n, p1c, p2n, p2c)
        print (d)

    def game_winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name

    def play_game(self):
        cards = self.deck.cards
        print("Let's play War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play: "
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            elif p2c > p1c:
                self.p2.wins += 1
                self.wins(self.p2.name)
            else:
                self.wins(self.tie.name)

        win = self.game_winner(self.p1, self.p2)
        print("War is over. {} wins!".format(win))


game = Game()
game.play_game()
