import random

from matplotlib import pyplot as plt


random.seed(147)
x = range(1000)

unif = []

for i in x:
    unif.append(random.uniform(0,1))

y = []

def mean(x):
    return sum(x) / len(x)

for i in x:
    y.append(mean(unif[0:i+1]))

plt.plot(x, y, color = 'black', linestyle = 'solid')
plt.title("Mean of Uniform dist")

y[999]