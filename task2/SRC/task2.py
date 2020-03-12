import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import radians,cos,sin


coordinates = open('Coordinates.txt', 'r')
coordinates = coordinates.read()
coordinates = coordinates.replace(' ','')
coordinates = coordinates.replace('}','{')
coordinates = coordinates.split('{')

try:sphere_index = coordinates.index('sphere:')+1
except:sphere_index = coordinates.index(',sphere:')+1
coordinates[sphere_index] = coordinates[sphere_index].replace('[','')
coordinates[sphere_index] = coordinates[sphere_index].replace('],',':')
sphere = coordinates[sphere_index].split(':')
center = sphere.index('center')+1
center = sphere[center].split(',')
cx,cy,cz = int(center[0]),int(center[1]),int(center[2])
radius = sphere.index('radius')+1
radius = float(sphere[radius])

try:line_index = coordinates.index('line:')+1
except:line_index = coordinates.index(',line:')+1
coordinates[line_index] = coordinates[line_index].replace('],','')
coordinates[line_index] = coordinates[line_index].replace(']','')
coordinates[line_index] = coordinates[line_index].replace('[',' ')
line = coordinates[line_index].split()

line_start = line[0].split(',')
line_start = [float(line_start[0]),float(line_start[1]),float(line_start[2])]

line_end = line[1].split(',')
line_end = [float(line_end[0]),float(line_end[1]),float(line_end[2])]

size = 10

sphere= []
fig = plt.figure()
ax = fig.add_subplot(111,projection = "3d")

segments = 32
for s in range(size+1):
    phi = s * radians(180) / size
    for segment in range(segments + 1):
        theta = segment * radians(360) / segments
        x = radius * cos(theta) * sin(phi)
        y = radius * sin(theta) * sin(phi)
        z = radius * cos(phi)
        sphere.append([x+cx, y+cy, z+cz])

line = np.linspace(line_start,line_end,num=43)
for x in range(len(sphere)):
    ax.scatter(sphere[x][0],sphere[x][1],sphere[x][2],c="r")

collision = False
for l in range(len(line)):
    for sp in range(len(sphere)):
        new_list = [int(i) for i in sphere[sp]]
        new_list2 = [int(i) for i in line[l]]
        if abs(new_list2[0]) <= abs(new_list[0]) and abs(new_list2[1]) <= abs(new_list[1]) and abs(new_list2[2]) <= abs(new_list[2]):
            ax.scatter(line[l][0], line[l][1], line[l][2], c="b")
            collision = True
            break

    if collision == False:
        ax.scatter(line[l][0],line[l][1],line[l][2],c="g")
    else: collision = False



plt.show()