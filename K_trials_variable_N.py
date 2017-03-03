import numpy as np
from matplotlib import pyplot as plt
import plane_process as pp
from statsmodels.stats.proportion import proportion_confint

def plot_multiple_plane_sizes(K, N_vector, conf_level = 0.95, null_prop = 0.5):
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

	plt.plot(N_vector, p_hats, 'ro', label = 'r$\hat{p}$')
	plt.plot(N_vector, lower_bounds, 'k_', label = 'lower score interval bound')
	plt.plot(N_vector, upper_bounds, 'k_', label = 'upper score interval bound')
	plt.fill_between(N_vector, lower_bounds, upper_bounds,\
					 facecolor = 'grey', alpha = 0.2)

	plt.plot(np.linspace(min(N_vector), max(N_vector), 1000),\
			 np.repeat([null_prop], repeats = 1000), color = 'k', ls = '--')

	plt.show()


#just for debugging...
if __name__ == '__main__':
	K = int(input("Choose number of trials at each N: "))
	plot_multiple_plane_sizes(K, N_vector = [int(b) for b in np.linspace(2,100, 99)],\
							  conf_level = 0.95, null_prop = 0.5)
