# user.py
from library import Base

class Derived(Base):
    def bar(self):
        #return self.foo()
        return 'bar'
