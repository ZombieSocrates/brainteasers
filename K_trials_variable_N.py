import numpy as np
from matplotlib import pyplot as plt
import plane_process as pp
from statsmodels.stats.proportion import proportion_confint
import os

def plot_multiple_plane_sizes(K, N_vector, conf_level = 0.95,\
							  null_prop = 0.5, subdir_name = None):
	'''
	Calculates the success rate p_hat of running K trials
	of the `plane_process.py` simulation, and plots
	these rates out for multiple plane sizes N.

	At the same time, builds a Wilson Score Interval
	around each of these success rates and plots out
	the lower and upper bounds of those success rates.

	For more on Wilson Score Intervals and why they are
	better than confidence intervals based on the normal 
	approximation to the binomial distribution:

	https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval

	The optional argument `subdir_name` allows the user to choose
	a subdirectory for saving the output plot.  This should be the name
	of a subdirectory relative to the directory from which you are running
	the script.  Leaving this as `None` will display the results
	instead of saving.
	'''
	lower_bounds = []
	p_hats = []
	upper_bounds = []

	for plane_size in N_vector:
		trials = [pp.plane_process(plane_size) for i in range(K)]
		lower, upper = proportion_confint(count = sum(trials), nobs = K,\
										  alpha = 1 - conf_level, method = 'wilson')
		lower_bounds.append(lower)
		p_hats.append(sum(trials)*1.0/K)
		upper_bounds.append(upper)

	# Plot out your sample proportions and the bounds of the confidence intervals.
	# Use fill between to shade in between the confidence interval.
	plt.plot(N_vector, p_hats, 'rx', label = r'$\hat{p}$')
	plt.plot(N_vector, lower_bounds, 'b_', label = 'lower bound')
	plt.plot(N_vector, upper_bounds, 'g_', label = 'upper bound')
	plt.fill_between(N_vector, lower_bounds, upper_bounds,\
					 facecolor = 'grey', alpha = 0.2)

	# Plot a dotted line for the null hypothesized proportion
	plt.plot(np.linspace(min(N_vector), max(N_vector), 1000),\
			 np.repeat([null_prop], repeats = 1000),'k--')

	# Set up ticks, labels, and titles to look pretty
	plt.xticks(N_vector, rotation = 45)
	plt.xlabel('Seats on Plane')
	plt.yticks(np.linspace(0.25,0.75,11))
	plt.ylabel('Confidence Interval around Proportion')
	plt.title('%s Trials with Planes of Varying Size' % K)
	plt.legend(loc = 'best')
	if subdir_name:
		target_dir = '/'.join([os.getcwd(), subdir_name])
		plotlabel = '%s_trials_%s_to_%s_seat_planes' % \
		(K, min(N_vector), max(N_vector))
		plt.savefig(target_dir + '/%s.png' % plotlabel, \
			dpi = plt.gcf().dpi)
	else:
		plt.show()


#just for debugging...
if __name__ == '__main__':
	pp.create_or_clean_dir('multiplane_plots')
	K = int(input("Choose number of trials at each N: "))
	plot_multiple_plane_sizes(K, N_vector = [int(b) for b in np.linspace(10,200, 20)],\
							  conf_level = 0.95, null_prop = 0.5, subdir_name = 'multiplane_plots')
