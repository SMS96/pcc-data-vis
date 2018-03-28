
def get_roll_product(die1, die2, number_of_rolls):
	"""Returns a list of products generated by rolling two dice"""
	results = []
	for val in range(number_of_rolls):
		roll_product = die1.roll() * die2.roll()
		results.append(roll_product)
	return results

def print_basic_summary(roll_results):
	"""Prints max, min, and total unique values for prelim check"""
	print("Minimum value: " + str(min(roll_results)))
	print("Maximum value: " + str(max(roll_results)))
	print("Unique values:\n" + str(set(roll_results)))
	print("Total Unique Values: " + str(len(set(roll_results))))
	
def populate_frequencies(roll_results):
	"""Generates a list of frequencies for each unique value in roll_results"""
	frequency_dist = []
	for val in range(min(roll_results), max(roll_results) + 1):
		frequency = roll_results.count(val)
		frequency_dist.append(frequency)
	return frequency_dist

