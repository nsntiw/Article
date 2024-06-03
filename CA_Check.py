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
        #ok
        np.add.at(net_fx, order_1st_half, temp_fx)
        np.subtract.at(net_fx, order_2nd_half, temp_fx)
        np.add.at(net_fy, order_1st_half, temp_fy)
        np.subtract.at(net_fy, order_2nd_half, temp_fy)
        
        #[ 0.00000000e+00 -2.00229000e-10 -9.43888558e-11 -1.41583284e-10-5.33944000e-10  0.00000000e+00]
        #[0, 0, 0, 1, 1, 2]
        #[1, 2, 3, 2, 3, 3]
        #[-9.43888558e-11 -5.33944000e-10  1.41583284e-10  0.00000000e+00]
        print(net_fx)
        print(net_fy)
        '''
        temp_fx, temp_fy = temp * dx, temp * dy
        temp_f = temp_fx + temp_fy
        np.add.at(net_fx, order_1st_half, temp_f)
        np.subtract.at(net_fy, order_2nd_half, temp_f)
        '''
        #---------------------------
        #ok
        len_planet_list = len(planet_list)
        logs[i*len_planet_list: i*len_planet_list+3] = x0[save_order0]
        logs[i*len_planet_list+3] = x1[save_order1]
        logs[i*len_planet_list+4: i*len_planet_list+7] = y0[save_order0]
        logs[i*len_planet_list+7] = y1[save_order1]

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