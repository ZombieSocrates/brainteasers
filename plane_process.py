import numpy as np

def plane_process(N):
    '''
    Performs one trial of the "crazy plane" process assuming a 
    plane with N seats.  For more information on the problem
    statement, see the following link:

    http://math.stackexchange.com/questions/5595/taking-seats-on-a-plane
    '''

    # Generate a plane with N seats and passengers indexed from 1 to N.
    passengers = [b for b in range(1, N + 1)]
    seats = [b for b in range(1, N + 1)]

    # Run the process for every passenger except the final one, because
    # the last passenger is the metric for success or failure
    for passenger in passengers[:-1]:
    	# First passenger always chooses randomly
    	if passenger == 1:
    		seats.remove(np.random.choice(seats,1).item())
    	else:
    		try:
    			# Any other passenger tries to find his/her seat,
    			seats.index(passenger)
    		except ValueError:
    			# but if occupied, he/she chooses randomly
    			seats.remove(np.random.choice(seats,1).item())
    		else:
    			seats.remove(passenger)
    	#After a passenger chooses a seat, remove him/her from the list.
    	passengers.remove(passenger)

    # If `passengers` and `seats` are equivalent at the end of this process, then
    # the final passenger has his/her seat.  For now, print "success", otherwise
    # print "failure."
    return 1 if passengers == seats else 0

