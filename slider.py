from pylab import *
import matplotlib.pyplot as plt
import numpy

def update(val):
    A = sA.val
    B = sB.val
    C = sC.val
    y_data = A*x_data*x_data + B*x_data + C
    par_plot.set_ydata(y_data)
    draw()


x_data = numpy.arange(-100,100,0.1);

fig = plt.figure(figsize=plt.figaspect(0.75))
ax = fig.add_subplot(1, 1, 1)
subplots_adjust(top=0.8)

ax.set_xlim(-100, 100);
ax.set_ylim(-100, 100);
ax.set_xlabel('X')
ax.set_ylabel('Y')

axsliderA = axes([0.12, 0.85, 0.16, 0.075])
sA = Slider(axsliderA, 'A', -1, 1.0, valinit=0.5)
sA.on_changed(update)

axsliderB = axes([0.43, 0.85, 0.16, 0.075])
sB = Slider(axsliderB, 'B', -30, 30.0, valinit=2)
sB.on_changed(update)

axsliderC = axes([0.74, 0.85, 0.16, 0.075])
sC = Slider(axsliderC, 'C', -30, 30.0, valinit=1)
sC.on_changed(update)

axes(ax)
A = 1;
B = 2;
C = 1;
y_data = A*x_data*x_data + B*x_data + C;

par_plot, = plot(x_data,y_data, lw=2, color='red')

show()
