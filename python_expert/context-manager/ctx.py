# ctx.py

from sqlite3 import connect
# from contextlib import contextmanager

with open('ctx.py') as f:
    pass

# with ctx() as x:
#     pass

# x = ctx().__enter__
# try:
#     pass
# finally:
#    x.__exit__


class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, *args):
        next(self.gen_inst, None)

@contextmanager
def template(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')

#template = contextmanager(template)

with connect('test.db') as conn:
    cur = conn.cursor()
    with template(cur):
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(1, 2)')
        for row in  cur.execute('select sum(x * y) from points'):
            print(row)
        for row in  cur.execute('select x , y from points'):
            print(row)
