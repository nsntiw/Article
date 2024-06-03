#from IOHandler import *
#from Plotting import *
from math import sqrt
from time import time
from numba import jit
import numpy as np

#@jit(forceobj = True)
def main(m, vx, vy, x, y, order_1st_half, order_2nd_half, 
            ts_over_m, dx, dy, temp, temp_fx, temp_fy, net_fx, 
            net_fy, logs, epoch, time_step):
    for i in range(epoch):
        dx = x[order_2nd_half] - x[order_1st_half]
        dy = y[order_2nd_half] - y[order_1st_half]
        temp = 6.67430e-11 * m[order_1st_half] * m[order_2nd_half] / (dx**2 + dy**2)**1.5
        temp_fx, temp_fy = temp * dx, temp * dy
        np.add.at(net_fx, order_1st_half, temp_fx)
        np.subtract.at(net_fx, order_2nd_half, temp_fx)
        np.add.at(net_fy, order_1st_half, temp_fy)
        np.subtract.at(net_fy, order_2nd_half, temp_fy)
        #---------------------------
        len_x = len(x)
        logs[i*len_x:(i+1)*len_x] = x
        logs[(i+1)*len_x:(i+2)*len_x] = y
        x += vx * time_step
        y += vy * time_step
        vx += net_fx * ts_over_m
        vy += net_fy * ts_over_m
        net_fx = np.zeros(len_x)
        net_fy = np.zeros(len_x)
