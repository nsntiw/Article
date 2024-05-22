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
