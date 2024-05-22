import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))# Get the absolute path of the script's directory
sys.path.append(os.path.dirname(SCRIPT_DIR))# Add the parent directory to PYTHONPATH
from IOHandler import *
from Plotting import *

from tqdm import tqdm# for progress bar
import sys #for restarting script
from time import time#for benchmarking
from itertools import combinations
from numba import njit, prange, jit
from math import sqrt
import numpy as np
from line_profiler import LineProfiler

#MAIN-----------------------------------------------
#USER INPUT-----------------------------------------------

PlanetsInstantaneous = []
PlanetsResults = []

IOHandler1 = IOHandler()
for i, planetList in enumerate(IOHandler1.readPlanetData()):
    print(planetList)
    #PlanetsInstantaneous.append(array('f', []))
    PlanetsInstantaneous.append([])
    for p in planetList:
        PlanetsInstantaneous[i].append(float(p))#mass,vx,vy,x,y,fx,fy
    PlanetsResults.append([])
time_step, epoch = int(IOHandler1.getUserInput("Enter the level of precision(recommended: 100)", "Enter an integer: ")), int(IOHandler1.getUserInput("Enter the numper of steps to simulate(recommended: 100000)", "Enter an integer: "))

#SIMULATION-----------------------------------------------
unique_permutations = list(combinations(range(len(PlanetsInstantaneous)), 2))
m0, m1, vx0, vx1, vy0, vy1, x0, x1, y0, y1 = [np.zeros(len(unique_permutations), dtype = float) for _ in range(10)] 
result = []
orderFirstHalf, orderSecondHalf = [np.zeros(len(unique_permutations), dtype = int) for _ in range(2)]

for i, e in enumerate(unique_permutations):
    m0[i], vx0[i], vy0[i], x0[i], y0[i] = PlanetsInstantaneous[e[0]]
    m1[i], vx1[i], vy1[i], x1[i], y1[i] = PlanetsInstantaneous[e[1]]
    orderFirstHalf[i], orderSecondHalf[i] = e

def main(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1,
         orderFirstHalf, orderSecondHalf, time_step_over_m0,
         time_step_over_m1, distancex, distancey, temp, resultF, result,
         fx, fy, net_fx, net_fy, epoch, time_step):
    for _ in range(epoch):#simulation loop, tqdm for progres bar
        #calculate distance
        distancex = x1 - x0
        distancey = y1 - y0
        #G*m0*m1/radus^3
        temp = 6.67430e-11 * m0 * m1 / (distancex**2 + distancey**2)**1.5
        
        fx, fy= temp * distancex, temp * distancey
        resultF = fx + fy
        np.add.at(net_fx, orderFirstHalf, resultF)
        np.subtract.at(net_fy, orderSecondHalf, resultF)
        
        
        '''
        fx, fy = temp * dx, temp * dy
        np.add.at(net_fx, orderFirstHalf, fx)
        np.subtract.at(net_fx, orderSecondHalf, fx)
        np.add.at(net_fy, orderFirstHalf, fy)
        np.subtract.at(net_fy, orderSecondHalf, fy)
        '''
        
        #---------------------------
        '''
        tempX = np.hstack((x0, x1))
        tempY = np.hstack((y0, y1))
        resultsX.append(np.unique(tempX))
        resultsY.append(np.unique(tempY))
        '''
        
        x0 += vx0 * time_step
        y0 += vy0 * time_step
        x1 += vx1 * time_step
        y1 += vy1 * time_step
        vx0 += net_fx[orderFirstHalf] * time_step_over_m0
        vy0 += net_fy[orderFirstHalf] * time_step_over_m0
        vx1 += net_fx[orderSecondHalf] * time_step_over_m1
        vy1 += net_fy[orderSecondHalf] * time_step_over_m1
        


if __name__ == "__main__":
    #lp = LineProfiler()
    #lp.add_function(main)
    #lp_wrapper = lp(main)
    #lp_wrapper(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1, epoch, time_step)
    #lp.print_stats()
    start = time()
    dx, dy, temp, temp_fx, temp_fy, net_fx, net_fy, resultF  = [np.zeros(len(m0), dtype = float) for _ in range(8)]
    ts_over_m0 = time_step/m0
    ts_over_m1 = time_step/m1
    main(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1, orderFirstHalf, orderSecondHalf, ts_over_m0, ts_over_m1,  dx, dy, temp, resultF, result, temp_fx, temp_fy, net_fx, net_fy, epoch, time_step)
    print(f"it/s: {epoch/(time()-start)}")
    #plot(PlanetsResults)
    #plotColorTest(PlanetsResults)
    #IOHandler1.writeResults(list_planet)
