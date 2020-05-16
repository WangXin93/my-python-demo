from minPQ import minPQ
import random

if __name__ == "__main__":
    q = minPQ()
    for _ in range(10):
        num = random.randint(0, 100)
        q.add(num)
        print("Add {}".format(num))

    for _ in range(10):
        print(q.removeSmallest())
