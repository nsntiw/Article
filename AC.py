from IOHandler import *
from Plotting import *
from math import sqrt
from time import time

class Planet:
    def __init__(self, input_list, time_step):
        self.m, self.vx, self.vy, self.x, self.y, self.net_fx, self.net_fy = input_list
        self.time_step_over_m = time_step / self.m
        self.history_x, self.history_y = [], []
    def accumulate_gravitational_force(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        temp = 6.67430e-11 * self.m * other.m / (dx**2 + dy**2)**1.5
        if dx != 0:
            fx = temp * dx
            self.net_fx += fx
            other.net_fx -= fx
        if dy != 0:
            fy = temp * dy
            self.net_fy += fy
            other.net_fy -= fy
    def velocity_euler(self):  # update velocity given force, mass and time_step
        new_vx = self.vx + self.net_fx * self.time_step_over_m
        new_vy = self.vy + self.net_fy * self.time_step_over_m
        return new_vx, new_vy
    def location_euler(self, time_step):  # update coordinate given current location, velocity and time_step
        new_x = self.x + self.vx * time_step
        new_y = self.y + self.vy * time_step
        return new_x, new_y
    def update_parameters(self, time_step):
        self.history_x.append(self.x)
        self.history_y.append(self.y)
        new_vx, new_vy = self.velocity_euler()
        new_x, new_y = self.location_euler(time_step)
        self.vx, self.vy = new_vx, new_vy
        self.x, self.y = new_x, new_y
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