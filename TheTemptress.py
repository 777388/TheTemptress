import math
import time
import matplotlib.pyplot as plt
import sys
bang = 0
for b in sys.argv[1]:
    bang += ord(b)
times = math.ceil(time.time())
x = lambda boobs: math.fabs(math.comb(times, int(boobs / bang)))
tempt = []
for i in range(math.ceil(time.time()) % bang):
    tempt.append(i)

plt.plot(list(map(x, tempt)))
plt.show()