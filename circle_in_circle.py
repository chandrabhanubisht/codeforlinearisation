import matplotlib
import scipy as sp
import numpy as np
from matplotlib import pyplot as plt
T=np.arange(0,10,.01)
omega=2
r=8
for t in T:
    a=r*sp.sin(omega*t)
    b=r*sp.cos(omega*t)

    R=4
    theta=np.arange(0,2*sp.pi,.01)
    print(theta)
    circle_x=[]
    circle_y=[]
    for i in theta:

        x=a+R*sp.cos(i)
        y=b+R*sp.sin(i)
        circle_x.append(x)
        circle_y.append(y)
    plt.plot(circle_x,circle_y)
    plt.pause(.0001)

plt.show()