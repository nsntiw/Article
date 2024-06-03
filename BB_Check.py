#from IOHandler import *
from Plotting import *
from math import sqrt
from time import time
'''
planetList = []#list of planet objects
IOHandler1 = IOHandler()
for rowList in IOHandler1.readPlanetData():#read the selected rows from the csv file
    print(rowList)#print each element for the user to check
    planetList.append(Planet(rowList))#since content is a dict it can be directly used to initialise planet objects
time_step, epoch = int(IOHandler1.getUserInput("Enter the level of precision(recommended: 100)", "Enter an integer: ")), int(IOHandler1.getUserInput("Enter the numper of steps to simulate(recommended: 100000)", "Enter an integer: "))
'''
def main(list_list, list_permutation_list, epoch, time_step):
    for _ in range(epoch):#simulation loop, tqdm for progres bar
        for p0, p1 in list_permutation_list:
            m0, _, _, x0, y0, _, _, _, _ = a = list_list[p0]
            m1, _, _, x1, y1, _, _, _, _ = b = list_list[p1]
            dx = x1 - x0
            dy = y1 - y0 
            temp = 6.67430e-11 * m0 * m1 / (dx**2 + dy**2)**1.5
            fx, fy = temp * dx, temp * dy
            a[5] += fx
            b[5] -= fx
            a[6] += fy
            b[6] -= fy
        for i, p in enumerate(list_list):
            m, vx, vy, x, y, net_fx, net_fy, time_step_over_m, history= p
            p[8].extend((x, y))
            new_vx = vx + net_fx * time_step_over_m
            new_vy = vy + net_fy * time_step_over_m
            new_x = x + vx * time_step
            new_y = y + vy * time_step
            list_list[i] = [m, new_vx, new_vy, new_x, new_y, 0, 0, time_step_over_m, history]
'''
#if __name__ == "__main__":
    start = time()
    main()
    print(f"it/s: {epoch/(time()-start)}")
#    main()
#    plotOld(planetList)
    #IOHandler1.writeResults(planetList)
'''