import matplotlib.pyplot as plt
import numpy as np
import timeit
from tqdm import tqdm# for progress bar
from itertools import combinations

import AA #The intuitive implementation
import AB #Reducing redundant accumulate_gravitational_force calls
import AC #Reducing redundant calculations
import AD #Class overhead?
import BA #Classless, dicts
import BB #Classless, lists
import CA #Vectorised, combinations order
import CB #Vectorised, original order

#Generate list of lists procedually, adding one element each
def gen_input(i, prev_list):
    return(prev_list[-1] + [[100.0,10,0,0,100*(i+1),0,0]])

#Triangular numbers as indexes for benchmark
#triangular_list = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 92, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666]
#triangular_list = [435, 465, 496, 528, 561, 595]
#triangular_list = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 92, 105, 120, 136, 153, 171, 190, 210]
triangular_list = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 92]
#triangular_list = [1, 3, 6, 10, 15, 21, 28]

#Simulation variables
numEntry, time_step, epoch = triangular_list[-1] + 1, 1, 10
g = globals()

#Input_list for index 0
input_lists = [[[100.0,10,0,0,0,0,0]]] #mass, vx, vy, x, y, net_fx, net_fy

#Initialise lists for AA-BB
AA_planet_lists, AB_planet_permutation_lists, AC_planet_lists, AC_planet_permutation_lists, AD_planet_lists, AD_planet_permutation_lists, BA_planet_lists, BA_planet_permutation_lists, BB_planet_lists, BB_planet_permutation_lists = [], [], [], [], [], [], [], [], [], []

#Initialise lists for CA
m0, m1, vx0, vx1, vy0, vy1, x0, x1, y0, y1, ts_over_m0, ts_over_m1, log, order_1st_half, order_2nd_half, dx, dy, temp, temp_fx, temp_fy, net_fx, net_fy, temp_f = [[] for _ in range(23)]

#Initialise lists for CB
m, vx, vy, x, y, ts_over_m, log1 = [[] for _ in range(7)]

#Fill lists with data
for i in tqdm(range(numEntry)):
    #AA
    AA_planet_lists.append([AA.Planet(e) for e in input_lists[-1]])
    #AB
    AB_planet_permutation_lists.append(list(combinations((AA_planet_lists[-1]), 2)))
    #AC
    AC_planet_lists.append([AC.Planet(e, time_step) for e in input_lists[-1]])
    AC_planet_permutation_lists.append(list(combinations((AC_planet_lists[-1]), 2)))
    #AD
    AD_planet_lists.append([AD.Planet(e, time_step) for e in input_lists[-1]])
    AD_planet_permutation_lists.append(list(combinations((AD_planet_lists[-1]), 2)))
    #BA
    BA_planet_lists.append([{"m" : e[0], "vx" : e[1],"vy" : e[2],"x" : e[3],"y" : e[4],"net_fx" : e[5],"net_fy" : e[6], "ts_over_m" : e[0]/time_step, "log_x" : [], "log_y" : []} for e in input_lists[-1]])
    BA_planet_permutation_lists.append(list(combinations((BA_planet_lists[-1]), 2)))
    #BB
    BB_planet_lists.append([e + [e[0]/time_step, []] for e in input_lists[-1]])
    BB_planet_permutation_lists.append(list(combinations(range(len(BB_planet_lists[-1])), 2)))
    #CA
    #Append numpy arrays to each element
    index_permutations = list(combinations(range(len(input_lists[-1])), 2))
    m0.append(np.zeros(len(index_permutations), dtype=float))
    m1.append(np.zeros(len(index_permutations), dtype=float))
    vx0.append(np.zeros(len(index_permutations), dtype=float))
    vx1.append(np.zeros(len(index_permutations), dtype=float))
    vy0.append(np.zeros(len(index_permutations), dtype=float))
    vy1.append(np.zeros(len(index_permutations), dtype=float))
    x0.append(np.zeros(len(index_permutations), dtype=float))
    x1.append(np.zeros(len(index_permutations), dtype=float))
    y0.append(np.zeros(len(index_permutations), dtype=float))
    y1.append(np.zeros(len(index_permutations), dtype=float))
    order_1st_half.append(np.zeros(len(index_permutations), dtype=int))
    order_2nd_half.append(np.zeros(len(index_permutations), dtype=int))
    ts_over_m0.append(np.zeros(len(index_permutations), dtype=float))
    ts_over_m1.append(np.zeros(len(index_permutations), dtype=float))
    log.append(np.zeros(len(index_permutations) * epoch * 2, dtype=float))
    dx.append(np.zeros(len(index_permutations), dtype=np.float32))
    dy.append(np.zeros(len(index_permutations), dtype=np.float32))
    temp.append(np.zeros(len(index_permutations), dtype=np.float32))
    temp_fx.append(np.zeros(len(index_permutations), dtype=np.float32))
    temp_fy.append(np.zeros(len(index_permutations), dtype=np.float32))
    net_fx.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    net_fy.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    #Fill the numpy arrays with data
    for j, e in enumerate(index_permutations):
        m0[-1][j], vx0[-1][j], vy0[-1][j], x0[-1][j], y0[-1][j], _, _ = [float(ee) for ee in input_lists[-1][e[0]]]
        m1[-1][j], vx1[-1][j], vy1[-1][j], x1[-1][j], y1[-1][j], _, _ = [float(ee) for ee in input_lists[-1][e[1]]]
        order_1st_half[-1][j], order_2nd_half[-1][j] = e
    ts_over_m0[i], ts_over_m1[i] = time_step / m0[i], time_step / m1[i]
    #CB
    #Append numpy arrays to each element
    m.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    vx.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    vy.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    x.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    y.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    ts_over_m.append(np.zeros(len(input_lists[-1]), dtype=np.float32))
    log1.append(np.zeros(len(input_lists[-1]) * epoch * 2, dtype=np.float32))
    #Fill the numpy arrays with data
    for j, e in enumerate(input_lists[-1]):
        m[-1][j], vx[-1][j], vy[-1][j], x[-1][j], y[-1][j], _, _ = [np.float32(ee) for ee in e]
    ts_over_m[i]= time_step / m[i]
    #Recursively generate list of planets for each element
    input_lists.append(gen_input(i, input_lists))

#Define the command to time, which will run 10 times for each element in triangular_list
command0 = """AA.main(AA_planet_lists[{}], epoch, time_step)"""
command1 = """AB.main(AA_planet_lists[{}], AB_planet_permutation_lists[{}], epoch, time_step)"""
command2 = """AC.main(AC_planet_lists[{}], AC_planet_permutation_lists[{}], epoch, time_step)"""
command3 = """AD.main(AD_planet_lists[{}], AD_planet_permutation_lists[{}], epoch, time_step)"""
command4 = """BA.main(BA_planet_lists[{}], BA_planet_permutation_lists[{}], epoch, time_step)"""
command5 = """BB.main(BB_planet_lists[{}], BB_planet_permutation_lists[{}], epoch, time_step)"""
command6 = """CA.main(m0[{}], m1[{}], vx0[{}], vy0[{}], x0[{}], y0[{}], vx1[{}], vy1[{}], x1[{}], 
y1[{}], order_1st_half[{}], order_2nd_half[{}], ts_over_m0[{}], ts_over_m1[{}], dx[{}], 
dy[{}], temp[{}], temp_fx[{}], temp_fy[{}], net_fx[{}], net_fy[{}], log[{}], epoch, 
time_step)"""
command7 = """CB.main(m[{}], vx[{}], vy[{}], x[{}], y[{}], order_1st_half[{}], order_2nd_half[{}], ts_over_m[{}], dx[{}], 
dy[{}], temp[{}], temp_fx[{}], temp_fy[{}], net_fx[{}], net_fy[{}], log1[{}], epoch, 
time_step)"""
#commands = [command0, command1, command2, command3, command4, command5]
commands = [command6, command7]
#commands = [command0, command1, command2, command3,command4, command5]
#commands = [command6]

plt.figure(figsize=(10, 6))
result_times = [[] for _ in range(len(commands))]
colors = ['red', 'green', "blue", 'orange', 'purple', 'cyan', 'yellow']
labels = ["AA", "AB", "AC", "AD", "BA", "BB", "CA", "CB"]
#Benchmark
for i in tqdm(triangular_list):
    for _ in range(10):
        for j, command in enumerate(commands):
            args = command.count('{}')
            result_time = timeit.timeit(command.format(*(i,) * args), globals=g, number=1)
            result_times[j].append(result_time)
            plt.plot(i, result_time, 'or', markersize = 2, color = colors[j])

#Plotting execution time
for result_time, label, color in zip(result_times, labels, colors):
    coeffs = np.polyfit(triangular_list, [np.mean(result_time[i:i+10]) for i in range(0, len(result_time), 10)], 4)
    p = np.poly1d(coeffs)
    x_values = np.linspace(min(triangular_list), max(triangular_list), 100)  # Generate 100 x values between min and max
    y_values = p(x_values)  # Calculate corresponding y values using polynomial fit
    plt.plot(x_values, y_values, '-', color=color, label=label)
    if(label == "AA"):
        #Print first command for poly fit
        print(x_values)
        print(y_values)
plt.xlabel('Number of bodies')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time')
plt.xticks(triangular_list)
plt.grid(True)
plt.legend()
plt.show()

#Plotting % speed up
for result_time, label, color in zip(result_times, labels, colors):
    mean_times0 = [np.mean(result_times[0][i:i+10]) for i in range(0, len(result_times[0]), 10)]
    mean_times = [np.mean(result_time[i:i+10]) for i in range(0, len(result_time), 10)]
    speed_up = [(1/mean_times[i] / (1/mean_times0[i]) - 1)* 100 for i in range(len(mean_times))]
    plt.plot(triangular_list, speed_up, '-', color=color, label=label)
    #Print speed up of the last command vs the first command
    print(((1/mean_times[-1]) / (1/mean_times0[-1]) - 1) *100)
plt.xlabel('Number of bodies')
plt.ylabel('% Speedup')
plt.title('% Speedup')
plt.xticks(triangular_list)
plt.grid(True)
plt.legend()
plt.show()