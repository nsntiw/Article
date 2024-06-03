from IOHandler import *
from Plotting import *
from itertools import combinations
import BB
import CA_Check
import CB

planet_list = [[100.0,0,0,100,100, 0, 0], [200.0,0,0,100,0, 0, 0], [300.0,0,0,0,100, 0, 0], [400.0,0,0,0,0, 0, 0]]
epoch, time_step = 1000000,10

index_permutations = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
'''
#Check BB plot
BB_planet_list = []
BB_planet_list = [e + [time_step/e[0], []] for e in planet_list]
BB_planet_permutation_lists = list(combinations(range(len(BB_planet_list)), 2))
BB.main(BB_planet_list, BB_planet_permutation_lists, epoch, time_step)
'''

#Check CA plot
m0, m1, vx0, vx1, vy0, vy1, x0, x1, y0 ,y1, ts_over_m0, ts_over_m1, dx, dy, temp, temp_fx, temp_fy = [np.zeros(len(index_permutations), dtype=float) for _ in range(17)]
order_1st_half, order_2nd_half = [np.zeros(len(index_permutations), dtype=int) for _ in range(2)]
net_fx, net_fy = [np.zeros(len(planet_list), dtype=float) for _ in range(2)]
log = np.zeros(len(planet_list) * epoch * 2, dtype=float)
# Fill the arrays with data
for j, e in enumerate(index_permutations):
    m0[j], vx0[j], vy0[j], x0[j], y0[j], _, _ = [float(ee) for ee in planet_list[e[0]]]
    m1[j], vx1[j], vy1[j], x1[j], y1[j], _, _ = [float(ee) for ee in planet_list[e[1]]]
    order_1st_half[j], order_2nd_half[j] = e
ts_over_m0, ts_over_m1 = time_step / m0, time_step / m1

save_order0 = np.array([0,3,5], dtype=int)
save_order1 = np.array([2], dtype=int)


CA_Check.main(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1, order_1st_half, order_2nd_half, 
         ts_over_m0, ts_over_m1, dx, dy, temp, temp_fx, temp_fy, net_fx, 
         net_fy, log, epoch, time_step, planet_list, save_order0, save_order1)
plot_CA_Check(log)


#Check CB plot
m, vx, vy, x, y, ts_over_m, log1, dx1, dy1, temp1, temp_fx1, temp_fy1, net_fx1, net_fy1 = [np.zeros(len(planet_list), dtype=np.float32) for _ in range(14)]
dx1, dy1, temp1, temp_fx1, temp_fy1 = [np.zeros(len(index_permutations), dtype=np.float32) for _ in range(5)]
log1 = np.zeros(len(planet_list) * epoch * 2, dtype=float)
order_1st_half, order_2nd_half = [np.zeros(len(index_permutations), dtype=int) for _ in range(2)]
#Fill the numpy arrays with data
for j, e in enumerate(planet_list):
    m[j], vx[j], vy[j], x[j], y[j], _, _ = [np.float32(ee) for ee in e]
for j, e in enumerate(index_permutations):
    order_1st_half[j], order_2nd_half[j] = e
ts_over_m = time_step / m
CB.main(m, vx, vy, x, y, order_1st_half, order_2nd_half, 
            ts_over_m, dx1, dy1, temp1, temp_fx1, temp_fy1, net_fx1, 
            net_fy1, log1, epoch, time_step)
plot_CA_Check(log1)
