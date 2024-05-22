from IOHandler import *
from Plotting import *
from Article import *

from line_profiler import LineProfiler
planet_list = [Planet([100.0,0,0,100,100]), Planet([200.0,0,0,100,0]), Planet([300.0,0,0,0,100]) ,Planet([400.0,0,0,0,0])]
epoch, time_step = 1,1
lp = LineProfiler()
lp.add_function(Planet.accumulate_gravitational_force)
lp.add_function(Planet.velocity_euler)
lp.add_function(Planet.location_euler)
lp.add_function(Planet.update_parameters)
lp_wrapper = lp(main)
lp_wrapper(planet_list, epoch, time_step)
lp.print_stats()