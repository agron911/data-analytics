#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

x1 = x2 = np.arange(-5,15,1)
x1,x2 =np.meshgrid(x1,x2)

z = 1/2*x1**2

azim = -60
elev = 30


plt.ion()
for i in range(30000):
    plt.clf()
    fig = plt.gcf()
    ax = fig.gca(projection='3d')
    ax.view_init(elev,azim)

    
    ax.plot_surface(x1,x2,z,cmap='rainbow')
    plt.pause(0.1)
              
    elev,azim = ax.elev, ax.azim          
                 
                 
    plt.ioff()
    
    z=  z-x1+4*x2
    
plt.show()


# In[ ]:




