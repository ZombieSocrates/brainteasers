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
	#fig = plt.figure()
	#for subplot in range(pltgrid_x * pltgrid_y):
	#	ax = plt.subplot(pltgrid_x, pltgrid_y, subplot + 1)
	trial_index = np.arange(1, K + 1)
	trial_values = np.zeros(K)

	for i in range(len(trial_values)):
		trial_values[i] = pp.plane_process(N)

	#		ax.plot(x = trial_index, y = (np.cumsum(trial_values)*1.0)/trial_index)
	#		ax.set_xlim(0,K)
	#		ax.set_ylim(0,1)

	#plt.show()
	return trial_index, np.cumsum(trial_values)/trial_index


#Just for debugging...
if __name__ == '__main__':
	X, Y = plot_cumulative_plane_processes(4, 10, pltgrid_x = 1, pltgrid_y = 1)
	plt.plot(X,Y, 'bo')
	plt.xlim(min(X), max(X))
	plt.ylim(0,1)
	plt.show()