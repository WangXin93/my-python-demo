""" This is an module string. """

from datetime import datetime


def sieve(maximum: int):
    """Print prime before MAX. """
    lst = [True for _ in range(maximum)]
    for i in range(2, maximum):
        if lst[i]:
            print(i)
            for j in range(i * i, maximum, i):
                lst[j] = False


def current_time():
    now = datetime.now()
    print("Now is {}".format(now))


if __name__ == "__main__":
    current_time()
    sieve(10)
