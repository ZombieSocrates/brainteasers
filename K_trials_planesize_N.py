import numpy as np
from matplotlib import pyplot as plt 
import plane_process as pp
import os

def plot_cumulative_plane_processes(K, N, pltgrid_x = 1, pltgrid_y = 1,\
									subdir_name = None):
	'''
	Performs K trials of the "crazy plane" process defined in the
	`plane_process.py` module for a plane with N seats.  Returns plots of
	the cumulative success rate for these K trials.

	The arguments pltgrid_x and pltgrid_y allow for a repeat of the 
	entire process listed above x * y times.  Defaults to a single
	one-by-one plot

	The optional argument `subdir_name` allows the user to choose
	a subdirectory for saving the output plot.  This should be the name
	of a subdirectory relative to the directory from which you are running
	the script.  Leaving this as `None` will display the results
	instead of saving.
	'''
	# Define shared parts of all visuals: the entire figure, 
	# an outer subplot, and the X axis.
	fig = plt.figure()
	outer = fig.add_subplot(1,1,1)
	X = np.arange(1, K + 1)

	# Plot out the subplots for all batches of trials.
	for b in range(pltgrid_x * pltgrid_y):
		ax = fig.add_subplot(pltgrid_x, pltgrid_y, b + 1)
		Y = np.array([pp.plane_process(N) for i in X])
		ax.plot(X, np.cumsum(Y) * 1.0/X, 'bo' if K <= 10 else 'b-')
		ax.set_xlim(min(X), max(X))
		ax.set_ylim(0,1)
		cum_prob = sum(Y) * 1.0/len(Y)
		ax.set_title("Success Rate: %.2f" % cum_prob)

	# Outer subplot was only there to set shared axis labels.
	# This just clears everything out and sets the text.
	outer.spines['top'].set_color('none')
	outer.spines['bottom'].set_color('none')
	outer.spines['right'].set_color('none')
	outer.spines['left'].set_color('none')
	outer.tick_params(labelcolor = 'w', top = 'off', bottom = 'off',\
					  left = 'off', right = 'off')
	outer.set_xlabel('Number of Trials')
	outer.set_ylabel('Success Rate')

	# Set overall title and provide more space for it.
	plt.suptitle("Crazy Plane with %s Seats: %s Batches of %s Trials"\
                  % (N, pltgrid_x * pltgrid_y, K))
	plt.tight_layout()
	plt.subplots_adjust(top = 0.85)
	
	# Save the plot in given subdirectory, or show it if no subdir given
	if subdir_name:
		target_dir = '/'.join([os.getcwd(), subdir_name])
		plotlabel = '%s_trials_%s_seats_plots' % (K,N)
		fig.savefig(target_dir + '/%s.png' % plotlabel, dpi = fig.dpi)
	else:
		plt.show()

if __name__ == '__main__':
	# Create a subdirectory of cwd to save off plots called 'plots'
	pp.create_or_clean_dir('plots')
	N = int(input("Choose seats on plane: "))
	K = int(input("Choose number of trials: "))
	print("Running four batches of trials with above specifications")
	plot_cumulative_plane_processes(K, N, pltgrid_x = 2, pltgrid_y = 2,\
									subdir_name = 'plots')

'''
TO DO:
* Maybe size the number of plots dynamically, so that it gets as close to 
an n by n square as possible?
'''
	