# crazy-plane

**Problem Statement**
Imagine there are a 100 people in line to board a plane that seats 100. The first person in line realizes he lost his boarding pass so when he boards he decides to take a random seat instead. Every person that boards the plane after him will either take their "proper" seat, or if that seat is taken, a random seat instead.

This is a problem that you can find stated in many places, [including but not limited to here](http://math.stackexchange.com/questions/5595/taking-seats-on-a-plane). Some goals that I have in this repo:

* Write a generic function that emulates this process with a plane of arbitrary size N
* Write a master function that repeats K trials of this process and plots out the cumulative probability of success
* Perhaps write a similar graphing function that shows how the probability of success fluctuates with plane size N

Using Python 3.6.  Likely package dependencies will be matplotlib and maybe numpy...
