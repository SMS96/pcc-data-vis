import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a RandomWalk object and populate it with values
data_points = 5 * (10 ** 4)

rw = RandomWalk(data_points)
rw.fill_walk()

#Set the size of the plotting window
plt.figure(figsize=(10, 6), dpi=128) #10 inches by 6 inches

#Apply color map to scatter plot to show direction of random walk
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
	cmap=plt.cm.Blues, edgecolor='none', s=1)

#Emphasize the first and last points
plt.scatter(0, 0, c='green', edgecolor='none', s=100)	#first point
plt.scatter(rw.x_values[-1], rw.y_values[-1], edgecolor='none', s=100, c='red')

#Removing axes to emphasize trend over actual values
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

#Show the plot only after all other changes have been made
plt.show()