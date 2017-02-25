import numpy as np
from matplotlib import pyplot as plt 
import plane_process as pp 

def plot_cumulative_plane_processes(K, N, pltgrid_x = 1, pltgrid_y = 1):
	'''
	Performs K trials of the "crazy plane" process defined in the
	`plane_process.py` module for a plane with N seats.  Returns plots of
	the cumulative success/failure ratio for these K trials.

	The arguments pltgrid_x and pltgrid_y allow for a repeat of the 
	entire process listed above x * y times.  Defaults to a single
	one-by-one plot
	'''

	X = np.arange(1, K + 1)

	for b in range(pltgrid_x * pltgrid_y):
		ax = plt.subplot(pltgrid_x, pltgrid_y, b + 1)
		Y = np.array([pp.plane_process(N) for i in X])
		# Plots out individual points if number of trials K
		# <= 10, otherwise plots a line
		ax.plot(X, np.cumsum(Y)*1.0/X, 'bo' if K <= 10 else 'b-')
		ax.set_xlim(min(X), max(X))
		ax.set_ylim(0,1)

	plt.show()


#Just for debugging...
if __name__ == '__main__':
	plot_cumulative_plane_processes(100, 100, pltgrid_x = 2, pltgrid_y = 2)



'''
TO DO:

* Add informative labels for the figure returned by `plot_cumulative_plane_process`
* Change the function so that it saves the file to a .png, perhaps clearing out any 
  extant png files as well.
'''
	