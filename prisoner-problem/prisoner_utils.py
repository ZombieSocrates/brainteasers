import numpy as np
import ipdb

def create_drawer_array(N):
	'''Returns a randomly sorted array from 0 through N-1 representing  
	the drawers the prisoners choose from.
	'''
	return np.random.permutation(N)

def n_random_choices(prisoner_index, drawer_array, choice_prop = 0.5):
	'''A prisoner with a input index chooses a certain number of
	drawers from an input array. This function will return 1 if
	the prisoner chooses a drawer matching his number, 0 otherwise

	By default, number of choices each prisoner makes will be half
	of the number of drawers
	'''
	n = int(choice_prop * len(drawer_array))
	choices = np.random.choice(drawer_array, size = n, replace = False)
	return len(np.where(choices == prisoner_index)[0])

if __name__ == '__main__':
	inmates = 100
	drawers = create_drawer_array(inmates)
	
	for prisoner in np.arange(inmates):
		print("Prisoner index {}".format(prisoner))
		choices = n_random_choices(prisoner, drawers)
		if choices:
			print('Card successfully found')
		else:
			print('EVERYBODY DIES')
			break
