class Baller:
    all_players = []

    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)
        
    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False

class BallHog(Baller):
    def pass_ball(self, other_player):
        return False

ajay = Baller('Ajay', True)
surya = BallHog('Surya')
"""
len(Baller.all_players)
Baller.name
len(surya.all_players)
ajay.pass_ball()
ajay.pass_ball(surya)
ajay.pass_ball(surya)
BallHog.pass_ball(surya, ajay)
surya.pass_ball(ajay)
surya.pass_ball(surya, ajay)
"""

class TeamBaller(Baller):
    """
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    def pass_ball(self, other):
        if Baller.pass_ball(self, other):
            print('Yay!')
            return True
        else:
            print("I don't have the ball")
            return False

# Q2
class PingPongTracker:
    """
    >>> tracker1 = PingPongTracker()
    >>> tracker2 = PingPongTracker()
    >>> tracker1.next()
    1
    >>> tracker1.next()
    2
    >>> tracker2.next()
    1
    """
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True

    def has_seven(self):
        if self.index % 7 == 0:
            return True
        rest = self.index
        while rest:
           rest, last = rest // 10, rest % 10
           if last == 7:
               return True
        return False

    def next(self):
        if self.add:
            self.current += 1
        self.index += 1
        if self.has_seven():
            self.add = not self.add
        return self.current

# Q4
class Bird:
    def __init__(self, call):
        self.call = call
        self.can_fly = True
    def fly(self):
        if self.can_fly:
            return "Don't stop me now!"
        else:
            return "Ground control to Major Tom..."
    def speak(self):
        print(self.call)

class Chicken(Bird):
    def speak(self, other):
        Bird.speak(self)
        other.speak()

class Penguin(Bird):
    can_fly = False
    def speak(self):
        call = "Ice to meet you"
        print(call)

andre = Chicken("cluck")
gunter = Penguin("noot")

andre.speak(Bird("coo"))
# cluck
# coo
andre.speak()
# Error
gunter.fly()
# "Don't stop me now!"
andre.speak(gunter)
# cluck
# Ice to meet you
Bird.speak(gunter)
# noot
