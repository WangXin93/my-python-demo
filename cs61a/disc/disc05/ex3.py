class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def __inti__(self, name, owner):
        Pet.__init__(self, name, owner)
    def talk(self):
        print(self.name + " says wroof!")

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    def talk(self):
        print(self.name + " says meow!")
    def lose_life(self):
        """A cat can only lose a life if they
        have at least one life. When lives 
        reaches zero, 'is_live' becomes False.
        """
        if self.lives:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False

class NoisyCat(Cat):
    def talk(self):
        for _ in range(2):
            Cat.talk(self)

doudou = Dog('doudou', 'WangX')
doudou.talk()
tom = Cat('tom', 'WangX')
tom.talk()
ntom = NoisyCat('ntom', 'WangX')
ntom.talk()