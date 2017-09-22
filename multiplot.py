from time import sleep
from threading import Thread
import matplotlib.pyplot as plt

def show():
	plt.plot(range(10))
	plt.show()

def close(time):
	sleep(time)
	plt.close()

thread1 = Thread(target=close, args=(5,))

thread1.start()
show()
