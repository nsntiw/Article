#from IOHandler import *
#from Plotting import *
from math import sqrt
from time import time
from numba import jit
import numpy as np

def main(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1, order_1st_half, order_2nd_half, 
         time_step_over_m0, time_step_over_m1, dx, dy, temp, temp_fx, temp_fy, net_fx, 
         net_fy, logs, epoch, time_step):
    for i in range(epoch):
        dx, dy = x1 - x0, y1 - y0
        temp = 6.67430e-11 * m0 * m1 / (dx**2 + dy**2)**1.5
        temp_fx, temp_fy = temp * dx, temp * dy
        np.add.at(net_fx, order_1st_half, temp_fx)
        np.subtract.at(net_fx, order_2nd_half, temp_fx)
        np.add.at(net_fy, order_1st_half, temp_fy)
        np.subtract.at(net_fy, order_2nd_half, temp_fy)
        #---------------------------
        len_x0 = len(x0)
        logs[i*len_x0:(i+1)*len_x0] = x0
        logs[(i+1)*len_x0:(i+2)*len_x0] = y0

        x0 += vx0 * time_step
        y0 += vy0 * time_step
        x1 += vx1 * time_step
        y1 += vy1 * time_step
        vx0 += net_fx[order_1st_half] * time_step_over_m0
        vy0 += net_fy[order_1st_half] * time_step_over_m0
        vx1 += net_fx[order_2nd_half] * time_step_over_m1
        vy1 += net_fy[order_2nd_half] * time_step_over_m1