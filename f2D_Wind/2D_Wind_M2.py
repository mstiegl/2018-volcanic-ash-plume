import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#This feature tries to model 2D Wind distribution of ash particles
# 03.07.2018

#DECLARING INPUT PARAMETERS
# wind direction raster
w_direction = np.random.randint(low=0, high=8, size=(10,10))
# particle raster (volcanic ash in ppm)
particles = np.zeros((10,10))
iterations = range(0,10)
# volcanic ash in ppm that gets erupted with each timestep
eruption = [50000, 100000, 50000, 25000, 15000, 10000, 1000, 500, 250, 100]
# placement of volcano
origin = [5,5]
#diffusion/fallout factor over time
loss = 0.5
#--------------------------------------------------------------------------------------

#just for testing purposes, make middle be all the same
w_direction[4] = 3
w_direction[5] = 3
w_direction[6] = 3


def partTransport(w_direction, particles, eruption, origin):
    ''' calculates transport of particles trough wind'''

    i = 0
    j = 0
    q = 0

    rows = int(np.shape(particles)[0])
    cols = int(np.shape(particles)[1])
    print("Modeling process initiated, goint through {} iterations".format(max(iterations)+1))



    #start for-loop here to iterate
    for n in iterations:

        #create temporary array to save calculated time step
        temp_arr = np.zeros((rows, cols))

        #dynamic particle generation at volcano
        particles[origin[0], origin[1]] = eruption[q]
        print("timestep {}, erupting {}".format(q+1, eruption[q]))



        #start while loops here to do the calculations








        q += 1








    return particles




partTransport(w_direction, particles, eruption, origin)

