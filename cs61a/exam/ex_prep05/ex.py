class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

class Proletariat(Worker):
    greeting = 'Comrade'
    def work(self, other):
        other.greeting = self.greeting + ' ' + other.greeting
        other.work() # for revolution
        return other

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

class Dress:
    """What color is the dress?
    >>> blue = Dress('blue')
    >>> blue.look()
    'blue'
    >>> gold = Dress('gold')
    >>> gold.look()
    'gold'
    >>> blue.look() # 2 does not evenly divide 3; changes to gold
    >>> Dress('black').look()
    'black'
    >>> gold.look() # 2 does not evenly divide 5; changes to black
    >>> gold.look() # 3 evenly divides 6
    'black'
    >>> Dress('white').look()
    'white'
    >>> gold.look() # 4 evenly divides 8
    'black'
    >>> blue.look() # 3 evenly divides 9
    'gold'
    """
    seen = 0
    color = None
    def __init__(self, color):
        self.color = color
        self.seen = 0
    def look(self):
        Dress.seen = Dress.seen + 1
        self.seen = self.seen + 1
        if Dress.seen % self.seen == 0:
            Dress.color = self.color
            return self.color
        else:
            self.color = Dress.color

def play_round(starter, cards):
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    [1]
    >>> play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It's not your turn, player 3
    It's not your turn, player 0
    The round is over, player 1
    [1, 3]
    >>> play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It's not your turn, player 2
    [1, 3]
    """
    r = Round(starter)
    for who, card in cards:
        try:
            r.play(who, card)
        except AssertionError as e:
            print(e)
    return Round.winners

class Round:
    players, winners = 4, []
    def __init__(self, starter):
        self.starter, self.player, self.highest = starter, starter, -1
    def play(self, who, card):
        assert self.starter != self.player or self.highest<0, 'The round is over, player '+str(who)
        assert who == self.player, "It's not your turn, player "+str(who)
        self.player = (self.player + 1) % Round.players
        if card >= self.highest:
            self.highest, self.control = card, who
        if self.complete():
            self.winners.append(self.control)
    def complete(self):
        return self.player == self.starter and self.highest > 0
