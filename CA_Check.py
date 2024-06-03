#from IOHandler import *
#from Plotting import *
from math import sqrt
from time import time
from numba import jit
import numpy as np

def main(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1, order_1st_half, order_2nd_half, 
         time_step_over_m0, time_step_over_m1, dx, dy, temp, temp_fx, temp_fy, net_fx, 
         net_fy, temp_f, logs, epoch, time_step, planet_list, save_order0, save_order1):
    for i in range(epoch):
        dx = x1 - x0
        dy = y1 - y0
        temp = 6.67430e-11 * m0 * m1 / (dx**2 + dy**2)**1.5
        temp_fx, temp_fy = temp * dx, temp * dy
        np.add.at(net_fx, order_1st_half, temp_fx)
        np.subtract.at(net_fx, order_2nd_half, temp_fx)
        np.add.at(net_fy, order_1st_half, temp_fy)
        np.subtract.at(net_fy, order_2nd_half, temp_fy)
        #---------------------------
        len_planet_list = len(planet_list)
        start_idx = i * len_planet_list*2
        logs[start_idx:start_idx + 3] = x0[save_order0]
        logs[start_idx + 3] = x1[save_order1]
        logs[start_idx + 4:start_idx + 7] = y0[save_order0]
        logs[start_idx + 7] = y1[save_order1]

        x0 += vx0 * time_step
        y0 += vy0 * time_step
        x1 += vx1 * time_step
        y1 += vy1 * time_step
        vx0 += net_fx[order_1st_half] * time_step_over_m0
        vy0 += net_fy[order_1st_half] * time_step_over_m0
        vx1 += net_fx[order_2nd_half] * time_step_over_m1
        vy1 += net_fy[order_2nd_half] * time_step_over_m1
        net_fx = np.zeros(len_planet_list)
        net_fy = np.zeros(len_planet_list)

        