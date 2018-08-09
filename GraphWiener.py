import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def stochastic_process(runs,steps):

    x = np.linspace(0,steps,steps)

    rnd_incr = np.random.normal(0,1,[steps,runs])
    y  = np.cumsum(rnd_incr,axis=0)
    plt.figure(1)
    plt.plot(x,y)
    plt.show(1)
    return

runs = int(input("Specifiy number of simulated processes: "))
steps = int(input("Specifiy number of time steps: "))

stochastic_process(runs,steps)
