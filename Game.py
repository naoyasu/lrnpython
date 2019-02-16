# http://tinyurl.com/huwq8mw

class Game:
    def __init__(self):
        name1 = input("Player1's name")
        name2 = input("Player2's name")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "This round wins {} "
        w = w.format(winner)
        print(w)

    def draw(self, pln, plc, p2n, p2c):
        d = "{} draws {}, {} draws {}"
        d = d.format(pln, plc, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Start war")
        while len(cards) >= 2:
            m = "quit press q, play other key:"
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
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("Finish the game,{} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "draw"


    
            
        
