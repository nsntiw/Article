#from IOHandler import *
#from Plotting import *
from math import sqrt
from time import time

class Planet:
    def __init__(self, input_list, time_step):
        self.m, self.vx, self.vy, self.x, self.y, self.net_fx, self.net_fy = input_list
        self.ts_over_m = time_step / self.m
        self.log_x, self.log_y = [], []
    def accumulate_gravitational_force(self, other):
        m0, x0, y0 = self.m, self.x, self.y
        m1, x1, y1 = other.m, other.x, other.y
        dx = x1 - x0
        dy = y1 - y0
        temp = 6.67430e-11 * m0 * m1 / (dx**2 + dy**2)**1.5
        if dx != 0:
            fx = temp * dx
            self.net_fx += fx
            other.net_fx -= fx
        if dy != 0:
            fy = temp * dy
            self.net_fy += fy
            other.net_fy -= fy
    def update_parameters(self, time_step):
        vx, vy, x, y, net_fx, net_fy, ts_over_m  = self.vx, self.vy, self.x, self.y, self.net_fx, self.net_fy, self.ts_over_m
        self.log_x.append(x)
        self.log_y.append(y)
        self.vx, self.vy = vx + net_fx * ts_over_m, vy + net_fy * ts_over_m
        self.x, self.y = x + vx * time_step, y + vy * time_step
        self.net_fx = self.net_fy = 0

'''
planet_list = []#list of planet objects
IOHandler1 = IOHandler()
for rowList in IOHandler1.readPlanetData():#read the selected rows from the csv file
    print(rowList)#print each element for the user to check
    planet_list.append(Planet(rowList))#since content is a dict it can be directly used to initialise planet objects
time_step, epoch = int(IOHandler1.getUserInput("Enter the level of precision(recommended: 100)", "Enter an integer: ")), int(IOHandler1.getUserInput("Enter the numper of steps to simulate(recommended: 100000)", "Enter an integer: "))
'''

def main(planet_list, planet_permutation_list, epoch, time_step):
#def main():
    for _ in range(epoch):#simulation loop, tqdm for progres bar
        for p0, p1 in planet_permutation_list:
            p0.accumulate_gravitational_force(p1)
        for planet in planet_list:
            planet.update_parameters(time_step)

'''
#if __name__ == "__main__":
    start = time()
    main()
    print(f"it/s: {epoch/(time()-start)}")
#    main()
#    plotOld(planetList)
    #IOHandler1.writeResults(planetList)
'''