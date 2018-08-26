# library.py

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        #print("BaseMeta.__new__", cls, name, bases, body)
        if name != 'Base' and not 'bar' in body:
            raise TypeError('Bad user class')
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    def __init_subclass__(self, *a, **kw):
        print("init_subclass", a, kw)
        return super().__init_subclass__(*a, **kw)

#old_bc = __build_class__
#def my_bc(func, name, base=None,  **kw):
#    if base is Base:
#        print('Check if bar method defined')
#    if base is not None:
#        return old_bc(func, name, base, **kw)
#    return old_bc(func, name, **kw)
#
#import builtins
#builtins.__build_class__ = my_bc
