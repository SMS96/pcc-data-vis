import pygal

from die import Die

#Create two D6 die
die_1 = Die()
die_2 = Die()

#Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analyze the results
frequencies = []
min_result = 2			#true for any number of n-sided dice
max_result = die_1.num_sides + die_2.num_sides
for value in range(min_result, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = ("Results of rolling two D6 dice 1000 times.".title())
hist.x_labels = [str(val) for val in range(min_result, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual_2.svg')