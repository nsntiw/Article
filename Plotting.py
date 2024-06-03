import os
import matplotlib.pyplot as plt #for plotting result
import numpy as np


def plotOld(list_planet):
    plt.figure(figsize=(8, 8))#set plot size
    for index, element in enumerate(list_planet):#Loop over list of planets to get list of coordinates, list of coordinates added to plot
        plt.plot(element.plotX, element.plotY, label=f'Planet: {index}')
    plt.title('Planet Trajectories ', fontsize=10)#Plot title
    plt.xlabel('x-axis', fontsize=10)#Axis naming
    plt.ylabel('y-axis', fontsize=10)
    plt.legend()#Place line labels on plot

    i = 0
    while os.path.isfile(f'plot {i}.png'):#infinite loop, check if there are already pngs saved, increment png number till no duplicates found, save file then evit loop
        i += 1
    plt.savefig(f'plot {i}.png')

    plt.show()#show plot

def plot(list_planet):
    plt.figure(figsize=(8, 8))#set plot size
    for index, element in enumerate(list_planet):#Loop over list of planets to get list of coordinates, list of coordinates added to plot
        x = []
        y = []
        xv = []
        yv = []
        for x_coord, y_coord, xv_coord, yv_coord in zip(element[::4], element[1::4], element[2::4], element[3::4]):
            x.append(x_coord)
            y.append(y_coord)
            xv.append(xv_coord)
            yv.append(yv_coord)
        plt.plot(x, y, label=f'Planet: {index}')
    plt.title('Planet Trajectories ', fontsize=10)#Plot title
    plt.xlabel('x-axis', fontsize=10)#Axis naming
    plt.ylabel('y-axis', fontsize=10)
    plt.legend()#Place line labels on plot

    i = 0
    while os.path.isfile(f'plot {i}.png'):#infinite loop, check if there are already pngs saved, increment png number till no duplicates found, save file then evit loop
        i += 1
    plt.savefig(f'plot {i}.png')

    plt.show()#show plot

def plotColorTest(list_planet):
    plt.figure(figsize=(8, 8))#set plot size
    for index, element in enumerate(list_planet):#Loop over list of planets to get list of coordinates, list of coordinates added to plot
        x = []
        y = []
        xv = []
        yv = []
        for x_coord, y_coord, xv_coord, yv_coord in zip(element[::4], element[1::4], element[2::4], element[3::4]):
            x.append(x_coord)
            y.append(y_coord)
            xv.append(abs(xv_coord))
            yv.append(abs(yv_coord))
        xv = np.array(xv)
        plt.scatter(x, y, c = plt.cm.hot(xv/max(xv)), edgecolor='none', label=f'Planet: {index}')
        #plt.plot(x, y, label=f'Planet: {index}')
    plt.title('Planet Trajectories ', fontsize=10)#Plot title
    plt.xlabel('x-axis', fontsize=10)#Axis naming
    plt.ylabel('y-axis', fontsize=10)
    plt.legend()#Place line labels on plot

    i = 0
    while os.path.isfile(f'plot {i}.png'):#infinite loop, check if there are already pngs saved, increment png number till no duplicates found, save file then evit loop
        i += 1
    plt.savefig(f'plot {i}.png')

    plt.show()#show plot

def plot_CA_Check(logs):
    plt.figure(figsize=(8, 8))#set plot size
    x0 = []
    x1 = []
    x2 = []
    x3 = []
    y0 = []
    y1 = []
    y2 = []
    y3 = []
    for i in range(0, len(logs), 8):#Loop over list of planets to get list of coordinates, list of coordinates added to plot
        x0.append(logs[i])
        x1.append(logs[i + 1])
        x2.append(logs[i + 2])
        x3.append(logs[i + 3])
        y0.append(logs[i + 4])
        y1.append(logs[i + 5])
        y2.append(logs[i + 6])
        y3.append(logs[i + 7])
    plt.plot(x0, y0, label=f'Planet: {0}')
    plt.plot(x1, y1, label=f'Planet: {1}')
    plt.plot(x2, y2, label=f'Planet: {2}')
    plt.plot(x3, y3, label=f'Planet: {3}')
    plt.title('Planet Trajectories ', fontsize=10)#Plot title
    plt.xlabel('x-axis', fontsize=10)#Axis naming
    plt.ylabel('y-axis', fontsize=10)
    plt.legend()#Place line labels on plot

    i = 0
    while os.path.isfile(f'plot {i}.png'):#infinite loop, check if there are already pngs saved, increment png number till no duplicates found, save file then evit loop
        i += 1
    plt.savefig(f'plot {i}.png')

    plt.show()#show plot


def plot_BB_Check(list_planet):
    plt.figure(figsize=(8, 8))#set plot size
    for index, element in enumerate(list_planet):#Loop over list of planets to get list of coordinates, list of coordinates added to plot
        x = []
        y = []
        for i in range(0, len(element[8]), 2):
            x.append(element[8][i])
            y.append(element[8][i+1])
        plt.plot(x, y, label=f'Planet: {index}')
    plt.title('Planet Trajectories ', fontsize=10)#Plot title
    plt.xlabel('x-axis', fontsize=10)#Axis naming
    plt.ylabel('y-axis', fontsize=10)
    plt.legend()#Place line labels on plot

    i = 0
    while os.path.isfile(f'plot {i}.png'):#infinite loop, check if there are already pngs saved, increment png number till no duplicates found, save file then evit loop
        i += 1
    plt.savefig(f'plot {i}.png')

    plt.show()#show plot