#from IOHandler import *
#from Plotting import *
from math import sqrt
from time import time
from numba import jit

#@jit(forceobj = True)
def main(m, vx, vy, x, y, order_1st_half, order_2nd_half, 
            time_step_over_m, dx, dy, temp, temp_fx, temp_fy, net_fx, 
            net_fy, temp_f, logs, epoch, time_step):
    for i in range(epoch):
        dx = x[order_2nd_half] - x[order_1st_half]
        dy = y[order_2nd_half] - y[order_1st_half]
        temp = 6.67430e-11 * m[order_1st_half] * m[order_2nd_half] / (dx**2 + dy**2)**1.5
        temp_fx, temp_fy = temp * dx, temp * dy
        temp_f = temp_fx + temp_fy
        np.add.at(net_fx, order_1st_half, temp_f)
        np.subtract.at(net_fy, order_2nd_half, temp_f)
        #---------------------------
        len_x = len(x)
        logs[i*len_x:(i+1)*len_x] = x
        logs[(i+1)*len_x:(i+2)*len_x] = y
        x = vx * time_step
        y = vy * time_step
        vx += net_fx * time_step_over_m
        vy += net_fy * time_step_over_m
