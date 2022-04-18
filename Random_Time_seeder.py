from random import sample
import numpy as np
import time as t
import datetime as dt

start = dt.datetime.now()
#delta = 1
current_time = start.strftime("%H:%M:%S")
i = int(t.time())+60
while (t.time() <= i):
    np.random.seed(int(t.time()))
    ra = np.array(sample(range(1, 81), k=20))
    fa = np.sort(ra)
    ra = fa
    print("Time: {}, Prediction: {}".format(current_time, ra))
    t.sleep(.15)
    with open("Drawing_(here).txt", 'a') as file:
        file.writelines(str([current_time, ra]) + "\n")