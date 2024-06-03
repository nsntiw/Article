from IOHandler import *
from Plotting import *
from itertools import combinations
import AA
import AB
import AC
import AD
import BA
import BB
import CA_Check
import CB

planet_list = [[100.0,0,0,100,100, 0, 0], [200.0,0,0,100,0, 0, 0], [300.0,0,0,0,100, 0, 0], [400.0,0,0,0,0, 0, 0]]
#epoch, time_step = 100000 ,10
epoch, time_step = 3 ,10

index_permutations = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

m0 = np.zeros(len(index_permutations), dtype=float)
m1 = np.zeros(len(index_permutations), dtype=float)
vx0 = np.zeros(len(index_permutations), dtype=float)
vx1 = np.zeros(len(index_permutations), dtype=float)
vy0 = np.zeros(len(index_permutations), dtype=float)
vy1 = np.zeros(len(index_permutations), dtype=float)
x0 = np.zeros(len(index_permutations), dtype=float)
x1 = np.zeros(len(index_permutations), dtype=float)
y0 = np.zeros(len(index_permutations), dtype=float)
y1 = np.zeros(len(index_permutations), dtype=float)

order_1st_half = np.zeros(len(index_permutations), dtype=int)
order_2nd_half = np.zeros(len(index_permutations), dtype=int)

time_step_over_m0 = np.zeros(len(index_permutations), dtype=float)
time_step_over_m1 = np.zeros(len(index_permutations), dtype=float)
logs = np.zeros(len(planet_list) * epoch * 2, dtype=float)

dx = np.zeros(len(index_permutations), dtype=float)
dy = np.zeros(len(index_permutations), dtype=float)
temp = np.zeros(len(index_permutations), dtype=float)
temp_fx = np.zeros(len(index_permutations), dtype=float)
temp_fy = np.zeros(len(index_permutations), dtype=float)
net_fx = np.zeros(len(planet_list), dtype=float)
net_fy = np.zeros(len(planet_list), dtype=float)
temp_f = np.zeros(len(index_permutations), dtype=float)
# Fill the arrays with data
for j, e in enumerate(index_permutations):
    m0[j], vx0[j], vy0[j], x0[j], y0[j], _, _ = [float(ee) for ee in planet_list[e[0]]]
    m1[j], vx1[j], vy1[j], x1[j], y1[j], _, _ = [float(ee) for ee in planet_list[e[1]]]
    order_1st_half[j], order_2nd_half[j] = e
time_step_over_m0, time_step_over_m1 = time_step / m0, time_step / m1

save_order0 = np.array([0,3,5], dtype=int)
save_order1 = np.array([2], dtype=int)

CA_Check.main(m0, m1, vx0, vy0, x0, y0, vx1, vy1, x1, y1, order_1st_half, order_2nd_half, 
         time_step_over_m0, time_step_over_m1, dx, dy, temp, temp_fx, temp_fy, net_fx, 
         net_fy, temp_f, logs, epoch, time_step, planet_list, save_order0, save_order1)

plotNew(logs)
