import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
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

	# Second line here was necessary to make the discrete tick marks show up on the plot
	# when using seaborn.  See "Known Issues" in Seaborn documentation and/or following
	# https://github.com/mwaskom/seaborn/issues/344
	sns.set_style('whitegrid')
	sns.set_context(rc ={'lines.markeredgewidth':1})

	# Plot out your sample proportions and the bounds of the confidence intervals.
	# Use fill between to shade in between the confidence interval.
	plt.plot(N_vector, p_hats, 'rx', label = 'Sample Success Rate ' + r'$\hat{p}$')
	plt.plot(N_vector, lower_bounds, 'b_', label = 'Lower Bound for True ' + r'$P(Success)$')
	plt.plot(N_vector, upper_bounds, 'g_', label = 'Upper Bound for True ' + r'$P(Success)$')
	plt.fill_between(N_vector, lower_bounds, upper_bounds,\
					 facecolor = 'grey', alpha = 0.2)

	# Plot a dotted line for the null hypothesized proportion
	plt.plot(np.linspace(min(N_vector), max(N_vector), 1000),\
			 np.repeat([null_prop], repeats = 1000),'k--')

	# Set up ticks, labels, and titles to look pretty
	plt.xticks(N_vector, rotation = 45, fontsize = 8)
	plt.xlabel('Seats on Plane')
	plt.yticks(np.linspace(0.25,0.75,11), fontsize = 8)
	plt.ylabel('%d%% Confidence Interval' % (conf_level * 100))
	plt.title('%s Trials with Crazy Planes of Varying Size' % K)
	plt.legend(loc = 'best', framealpha = 0.75, frameon = True, edgecolor = 'b')
	
	# Save the plot in given subdirectory, or show it if no subdir given
	if subdir_name:
		target_dir = '/'.join([os.getcwd(), subdir_name])
		plotlabel = '%s_trials_%s_to_%s_seat_planes' % \
		(K, min(N_vector), max(N_vector))
		plt.savefig(target_dir + '/%s.png' % plotlabel, \
			dpi = plt.gcf().dpi)
	else:
		plt.show()

if __name__ == '__main__':
	pp.create_or_clean_dir('multiplane_plots')
	K = int(input("Choose number of trials at each N: "))
	plot_multiple_plane_sizes(K, N_vector = [int(b) for b in np.linspace(10,200, 20)],\
							  conf_level = 0.95, null_prop = 0.5, subdir_name = 'multiplane_plots')
