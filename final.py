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

#MAIN-----------------------------------------------
#USER INPUT-----------------------------------------------
'''
PlanetsInstantaneous = []
PlanetsResults = []

IOHandler1 = IOHandler()
for i, planetList in enumerate(IOHandler1.readPlanetData()):
    print(planetList)
    planetList.append(0)
    planetList.append(0)
    #PlanetsInstantaneous.append(array('f', []))
    PlanetsInstantaneous.append([])
    for p in planetList:
        PlanetsInstantaneous[i].append(float(p))#mass,vx,vy,x,y,fx,fy
    PlanetsResults.append([])
time_step, epoch = int(IOHandler1.getUserInput("Enter the level of precision(recommended: 100)", "Enter an integer: ")), int(IOHandler1.getUserInput("Enter the numper of steps to simulate(recommended: 100000)", "Enter an integer: "))
'''

@njit(parallel=True)
def test(unique_permutations):
    for i in prange(len(unique_permutations)):
        p0, p1 = unique_permutations[i]
        #get instantaneous variables
        m0, _, _, x0, y0, fx0, fy0 = a = PlanetsInstantaneous[p0]
        m1, _, _, x1, y1, fx1, fy1 = b = PlanetsInstantaneous[p1]
        #calculate distance
        distancex = x1 - x0
        distancey = y1 - y0
        #G*m0*m1/radus^3
        temp = 6.67430e-11 * m0 * m1 / sqrt(distancex**2 + distancey**2)**3
        forcex, forcey = temp * distancex, temp * distancey
        a[5] = fx0 + forcex
        a[6] = fy0 + forcey
        b[5] = fx1 - forcex
        b[6] = fy1 - forcey

def calc(p0, p1):
    #get instantaneous variables
    m0, _, _, x0, y0, fx0, fy0 = a = PlanetsInstantaneous[p0]
    m1, _, _, x1, y1, fx1, fy1 = b = PlanetsInstantaneous[p1]
    #calculate distance
    distancex = x1 - x0
    distancey = y1 - y0
    #G*m0*m1/radus^3
    temp = 6.67430e-11 * m0 * m1 / (distancex**2 + distancey**2)**1.5
    forcex, forcey = temp * distancex, temp * distancey
    a[5] = fx0 + forcex
    a[6] = fy0 + forcey
    b[5] = fx1 - forcex
    b[6] = fy1 - forcey

def update_planet(p):
    m, vx, vy, x, y, fx, fy = p
    resultvx = vx + fx * time_step / m
    resultvy = vy + fy * time_step / m
    resultx = x + vx * time_step
    resulty = y + vy * time_step
    return [m, resultvx, resultvy, resultx, resulty, 0, 0]

    #SIMULATION-----------------------------------------------
def main(PlanetsInstantaneous, PlanetsResults, unique_permutations, epoch, time_step):
    #unique_permutations = list(combinations(range(len(PlanetsInstantaneous)), 2))
    for _ in range(epoch):#simulation loop, tqdm for progres bar
        for p0, p1 in unique_permutations:
            #get instantaneous variables
            m0, _, _, x0, y0, fx0, fy0 = a = PlanetsInstantaneous[p0]
            m1, _, _, x1, y1, fx1, fy1 = b = PlanetsInstantaneous[p1]
            #calculate distance
            distancex = x1 - x0
            distancey = y1 - y0
            #G*m0*m1/radus^3
            temp = 6.67430e-11 * m0 * m1 / (distancex**2 + distancey**2)**1.5
            forcex, forcey = temp * distancex, temp * distancey
            a[5] = fx0 + forcex
            a[6] = fy0 + forcey
            b[5] = fx1 - forcex
            b[6] = fy1 - forcey
        #[PlanetsResults[i].extend((p[3], p[4], p[1], p[2])) for i, p in enumerate(PlanetsInstantaneous)]
        #list(map(lambda p: PlanetsResults[p[0]].extend((p[1][3], p[1][4], p[1][1], p[1][2])), enumerate(PlanetsInstantaneous)))
        #PlanetsInstantaneous = list(map(update_planet, PlanetsInstantaneous))
        for i, p in enumerate(PlanetsInstantaneous):
            #get instantaneous variables
            m, vx, vy, x, y, fx, fy = p
            #save results
            PlanetsResults[i].extend((x,y))#marginally faster than two append
            #velocity euler
            #temp = time_step / m
            resultvx, resultvy = vx + fx * m, vy + fy * m
            #location euler
            resultx, resulty = x + vx * time_step, y + vy * time_step
            #override planet list
            PlanetsInstantaneous[i] = [m, resultvx, resultvy, resultx, resulty, 0, 0]
'''
    print(f"it/s: {steps/(time()-start)}")
    plot(PlanetsResults)
    #plotColorTest(PlanetsResults)
    #IOHandler1.writeResults(list_planet)

if __name__ == "__main__":
    #lp = LineProfiler()
    #lp.add_function(Planet.update)
    #lp_wrapper = lp(main)
    #lp_wrapper()
    #lp.print_stats()
    start = time()
    main()
    print(f"it/s: {epoch/(time()-start)}")
'''