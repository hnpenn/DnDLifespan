import random as rand
from statistics import mean, stdev
from matplotlib.pyplot import hist
rand.seed(89)

samples = 10000
tots_list = [0] * samples
for i in range(samples):
    r = rand.choices(range(1,7), k=4)
    r.sort()
    tot = sum(r[1:])
    tots_list[i] = tot

av = mean(tots_list)
std = stdev(tots_list)
hist(tots_list)