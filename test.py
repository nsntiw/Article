import numpy as np

order_1st_half, temp_f = [np.zeros(10, dtype = int) for _ in range(2)]
net_fx1, net_fx2 = [np.zeros(5, dtype = int) for _ in range(2)]

order_1st_half = [0,1,2,3,4,0,1,2,3,4]
temp_f = [1,2,3,4,5,6,7,8,9,10]
np.add.at(net_fx1, order_1st_half, temp_f)
print(net_fx1)
net_fx2[order_1st_half] += temp_f
print(net_fx2)