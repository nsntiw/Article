from IOHandler import *
from Plotting import *
from math import sqrt
from time import time

class Planet:
    def __init__(self, input_list):
        self.m, self.vx, self.vy, self.x, self.y, self.net_fx, self.net_fy = input_list
        self.net_fx, self.net_fy = 0, 0 
        self.log_x, self.log_y = [], []
    def accumulate_gravitational_force(self, other):
        radius = ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
        if other.x - self.x != 0:
            fx = 6.67430e-11 * self.m * other.m / radius**3 * (other.x - self.x)
            self.net_fx += fx
        if other.y - self.y != 0:
            fy = 6.67430e-11 * self.m * other.m / radius**3 * (other.y - self.y)
            self.net_fy += fy
    def velocity_euler(self, time_step):  # update velocity given force, mass and time_step
        new_vx = self.vx + self.net_fx * time_step / self.m
        new_vy = self.vy + self.net_fy * time_step / self.m
        return new_vx, new_vy
    def location_euler(self, time_step):  # update coordinate given current location, velocity and time_step
        new_x = self.x + self.vx * time_step
        new_y = self.y + self.vy * time_step
        return new_x, new_y
    def update_parameters(self, time_step):
        self.log_x.append(self.x)
        self.log_y.append(self.y)
        new_vx, new_vy = self.velocity_euler(time_step)
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

def main(planet_list, epoch, time_step):
#def main():
    for _ in range(epoch):#simulation loop, tqdm for progres bar
        for self in planet_list:
            for other in planet_list:
                self.accumulate_gravitational_force(other)
        for self in planet_list:
            self.update_parameters(time_step)

'''
if __name__ == "__main__":
    import cProfile
    import pstats
    cProfile.run('main(planet_list, epoch, time_step)', filename='profile_results')
    # Load the profiling results
    stats = pstats.Stats('profile_results')
    # Sort the statistics by cumulative time and print
    stats.sort_stats('cumulative')
    stats.print_stats()

    from line_profiler import LineProfiler
    planet_list = [Planet([100.0,0,0,100,100]),
                   Planet([200.0,0,0,100,0]),
                   Planet([300.0,0,0,0,100]),
                   Planet([400.0,0,0,0,0])]
    print(planet_list)
    epoch, time_step = 1,1
    lp = LineProfiler()
    lp.add_function(Planet.accumulate_gravitational_force)
    lp.add_function(Planet.update_parameters)
    lp.add_function(Planet.velocity_euler)
    lp.add_function(Planet.location_euler)
    lp_wrapper = lp(main)
    lp_wrapper(planet_list, epoch, time_step)
    lp.print_stats()
    
    #start = time()
    #main()
    #print(f"it/s: {epoch/(time()-start)}")
    #plotOld(planetList)
    #IOHandler1.writeResults(planetList)
'''