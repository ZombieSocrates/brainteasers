# Flipping a Coin on a Crazy Plane  
Simulating Your Way to Real Answers

I'm a big fan of brainteasers and happen to find quirky, counterintuitive mathematical truisms fascinating. I'd be lying if I said I hadn't spent a weekend figuring out why once you have 23 people in a room, [you're more likely than not to have at least one shared birthday.](https://en.wikipedia.org/wiki/Birthday_problem) At the same time, I don't consider myself particularly "good" at brainteasers, and can't say I'd perform as well as Bruce Willis in that [classic scene from Die Hard 3](https://www.youtube.com/watch?v=BVtQNK_ZUJg), even if Samuel L. was there to help me...

Luckily, there's a fairly simple way to improve your skill at almost anything: practice it, just as you might jog up stairs or run for long distances to build up stamina. But imagine if instead of having regular old running shoes, you had turbo-charged, bionic shoes that made it easier for you to run farther and push your distance limits. You'd build up your stamina for sure, and you might even run to parts of your neighborhood or city that you'd never explored before and see something cool.

While these turbo-shoes don't exist last time I checked, as a Data Scientist I can tell you that an analog to them exists when it comes to generating insights about a wide array of complex systems, from physical and biological processes and financial investments to winning your favorite board game or solving a little brainteaser. What's more, you already have everything you need to use this tool assuming you're reading this post from a computer.

What is this mysterious method I speak of? **Simulation!**

In my humble opinion, one of the "killer apps" of taking a data science-y approach to problem solving is as follows: "let computers do your dirty work for you." Setting up a quick simulation is one of the best examples of this principle at work: figure out what game you want to play, tell your computer the rules, and then have it play that game over and over again while aggregating the results in an easy-to-interpret format. This provides a way to tackle problems that are prohibitively complex and gain a good understanding of "long-run" phenomena, all while making a much better use of your time (unless you happen to be in the position to, say, [flip a coin 10,000 times](https://en.wikipedia.org/wiki/John_Edmund_Kerrich)).

In this post, I want to quickly demonstrate how trading the pen and paper for a little bit of Python helped me work out a brainteaser that I like to call the ["Crazy Plane" problem.](http://math.stackexchange.com/questions/5595/taking-seats-on-a-plane)

>Imagine there are a 100 people in line to board a plane with 100 seats. For convenience, let's say that person 1 has the ticket to seat 1, person 2 to seat 2, etc. Unfortunately, the first person in line is crazy and simply takes a random seat instead of looking at his ticket. Each person boarding after him will either take the "proper" seat, or will choose a random seat if hers is already occupied. _What is the probability that the last person to board the plane will end up in the correct seat?_

If you looked at the problem above for a little while, don't instantly see a way to "math it out," but don't want to just google the answer, then there's no need to ask your doctor about simulation because I already know it's right for you! You don’t need a stack of statistical skillz to solve this problem; all you need is a function.

## The Drawing Board
As is the case with many of the [problems we deal with here at Datascope](https://datascopeanalytics.com/work/), my first plan of attack was to pick up a pen and draw. Before tackling the 100-seat plane specified in the problem, I sketched out some trials with smaller planes just to get a sense of the scenario we're dealing with. Consider a tiny plane with just two seats and two passengers. When the first passenger chooses randomly, he'll either sit in his assigned seat or in the target passenger's seat, leaving the target passenger with a 50-50 shot of finding her seat unoccupied.  

*TO DO: add scan of hand-drawn probability tree with just two passengers*

We can draw out similar scenarios for planes with three seats and four seats. Every row in these diagrams represents the possible seat choices that the first, second, or nth passenger can make given the choices of previous passengers.  

*TO DO: add scan of hand-drawn probability trees with n = 3 and n = 4 passengers*

In looking at these base cases, a couple things stand out:
* The last passenger on the plane _only ever ends up in her seat or in the crazy guy's seat._ If one of the middle passengers "undoes" the crazy passenger's error by randomly selecting the crazy guy's seat, then everything else goes off without a hitch.    
* The probability that the last passenger gets the correct seat is 50 percent for each of these small planes. This gives us some inkling that the probability of the last passenger ending up in her assigned seat _may not depend on the number of people boarding the plane._

We have an idea of what will happen if we ramp up from our "tiny planes" to our full 100-seat crazy plane, which is great. Unfortunately, drawing these diagrams for larger planes quickly becomes intractable. I'd be lying if I said I didn't while away certain evenings drawing diagrams for five- and six-passenger planes, but I don't even want to think about larger diagrams.[ref]Especially considering that the 100-passenger diagram would have 2<sup>99</sup>, or about _634 octillion_, branches to draw, the smiley faces alone would take eons to perfect...[/ref].

## Simulating a Crazy Plane  
But here's the first of many bits of good news: we don't have to think about the 100-passenger diagram or calculate out all the ways in which passengers may be inconvenienced by prior randomness. Instead, we can lace up our metaphorical turbo-charged running shoes by plopping down in front of a computer (ironically) and letting a little bit of code do that work for us. Here's just one way of turning this brainteaser into an easily repeatable function: 

```python
import numpy as np

def plane_process(N):  
    '''
    Performs one trial of the "crazy plane" experiment
    for a plane with N seats
    '''
    
    # Generate a plane with seats and passengers indexed from 1 to N.
    passengers = [b for b in range(1, N + 1)]  	
    seats = [b for b in range(1, N + 1)]  
    
    # Board every passenger except the last one
    for passenger in passengers[:-1]:
    
        # The first passenger always chooses randomly...
        if passenger == 1:  
            seats.remove(np.random.choice(seats,1).item())
        else: 
        
            # Any other passenger looks for his seat...
            try:  
                seats.index(passenger)
            
            # ...will choose randomly if it’s already taken...
            except ValueError:  
                seats.remove(np.random.choice(seats,1).item()) 
            
            # ..but will take the correct seat if it isn’t.
            else:  
                seats.remove(passenger)
        
        # Once a passenger has boarded, remove her from the list
        passengers.remove(passenger) 
    
    # Check the last passenger against the last seat. If those values are the same, 
    # the last passenger got her seat!
    return 1 if passengers == seats else 0
```

We simulate passengers boarding the crazy plane by creating two identical lists representing the numbered passengers and their corresponding assigned seats. In the main loop, we board all passengers except the final one. As passengers take seats, the chosen numbers are removed from both lists. We know that the first passenger will always choose a seat randomly, so we make sure of that. Thereafter, each passenger tries to look up his seat, but will choose randomly if that seat has been removed from the list. Once all these choices have been made, we look at the last passenger and the last seat to see if there's a match, returning 1 for success and 0 for failure.

Voila! You can now simulate the crazy plane process for any size plane you like. Where do we go from here? Well, the crazy plane is chock full o' randomness, meaning that it is _unpredictable in the short run but predictable in the long run_ (just like rolling dice, or flipping coins). That is to say, the more times we observe a random process like the crazy plane, the better we’ll understand it. This is the real “secret sauce” of simulations: they generate much more information about the “long run” in a much shorter amount of time

To see what I mean, let’s simulate the long-run behavior of the 100-seat crazy plane. Each graph below shows the cumulative success rate (successful trials/total trials) of running the process 100 times.

![Image](singleplane_plots/100_trials_100_seats_plots.png)

Notice that to the leftmost region of each of these graphs (where the number of trials is still small), the blue line representing cumulative success rate fluctuates a lot, because random processes are "unpredictable over the short term." As we get closer to the full 100 trials, that fluctuation becomes much less pronounced and our success rate converges on the very same 50 percent that we saw in our “tiny plane” sketches. There's some variability of the success rates in each of the four "batches of experiments" above: we're generally within five percentage points of 50 percent, but never hit it on the nose.  How might this change if we bumped up the number of trials? Because we have code, this is an easy question to answer!

![Image](singleplane_plots_moarTrials/1000_trials_100_seats_plots.png)

Once we increase the number of simulations in each batch, the results come even closer to 50 percent. You can see in the far-right portion of each graph how our cumulative success rates have more or less flatlined. Put in a more general way: as we increase the "length of the long run," the impact of each individual experiment is minimized. This leaves us with a clearer picture of what's actually going on at scale: that this seemingly complex boarding process is no different than flipping a coin!  

## Don’t Just Calculate...Simulate!
At this point, let’s reflect on what we _haven’t_ done:   
* Opened a combinatorics textbook.
* Obtained an advanced math or stats degree.
* Filled blackboard upon blackboard with arcane equations a la A Beautiful Mind. 

Now, let’s reflect on what we **have** done:  
* Simulated our 100-seat crazy plane process thousands of times in a few seconds
* **Solved the problem**, for all intents and purposes
* Created something **extensible:** if we want more precision around our answer, we can simply run more simulations and tabulate new results.[ref]As these requirements grow in scale, we might need to rework the data structures employed in our function above, but that’s a topic for another blog post[/ref]
* Created something **customizable:** the function we created will work for any number of seats. Want to investigate a crazy plane with 50 seats? 150 seats? Just change N and you’re ready for lunatic lift-off!

In solving this brainteaser, we’ve also gotten a brief introduction to a technique called Monte Carlo methods, which is just a fancy term for simulating something a bunch of times to solve problems. If that description seems incredibly general, that's because simulations are _extensible_ and _customizable_ (as we’ve already seen). Simulation-based solutions to problems pop up in disciplines that are about as varied as the day is long. Here are just a couple of examples of simulation at work: 

1. If you wanted to estimate the value of π, you could do it with just a [one-by-one square, a circle inscribed within that square, and a uniform random number generator](https://am207.github.io/2017/wiki/basicmontercarlo.html#estimate-the-area-of-a-unit-circle)
2. Monte Carlo simulations are often employed to [program AI for various popular games](https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/)
3. If you happen to be an asset manager and want to understand how different portfolio allocations generate returns in various environments, [a tool like this one may be for you](https://www.portfoliovisualizer.com/monte-carlo-simulation)
4. There are shelves of textbooks devoted to simulation methods in branches of the physical sciences, including but not limited to [physics](https://books.google.com/books/about/Monte_Carlo_Simulation_in_Statistical_Ph.html?id=y6oDME582TEC&source=kp_cover),[fluid dynamics](https://books.google.com/books/about/Computer_Simulation_of_Liquids.html?id=O32VXB9e5P4C&source=kp_cover), [quantum mechanics](https://books.google.com/books/about/Monte_Carlo_Methods_in_Quantum_Problems.html?id=FTnqCAAAQBAJ&source=kp_cover), and [biology](http://www.intechopen.com/books/applications-of-monte-carlo-methods-in-biology-medicine-and-other-fields-of-science).

We demonstrated a simulation-based approach to solving a tidy little brainteaser that, if you weren't as stubborn of a nerd as I am, you probably could have just googled and found a litany of answers, explanations, and analytic solutions for.  That’s fine for a tidy little brainteaser. You may even have the math skillz to have solved this one without simulation, but any real problem will have many more degrees of complexity. In fact, it's not that hard to “untidy” our brainteaser a bit...

* What if there were not just one crazy passenger, but two, three, or more crazy passengers?
* What if those crazy passengers were dispersed randomly throughout the boarding line?
* What if a passenger randomly choosing a seat was more likely to choose certain seats than others? (i.e., perhaps the initial crazy is less likely to run way to the back of the plane and take seat 100 than he is to take a seat nearby, or any passenger finding her seat taken will choose the nearest unoccupied seat)

Minor tweaks like this will be difficult or require a PhD thesis to work into an analytic solution to the problem. By comparison, it’s easy to tweak our code above to accommodate any or all of the scenarios above, run a couple hundred or couple thousand more trials, and see how our inference changes. Now that we've explored one particular framing of the "crazy plane" problem and have some basic code to simulate the process, we have all the raw materials needed to formulate and test new hypotheses. No advanced training in statistics or combinatorics required, just a computer and some curiosity!

Additionally, simulations can illuminate the path to an analytic solution, much like the back of the textbook can help guide you from half a solution to a whole one. Given what our simulations showed us about the crazy plane problem, we might be emboldened to pick up the pencil and paper again to derive a general formula about why the probability is 50 percent. It may seem strange in this scenario, but let’s say our simulations were integrated within a larger application that needed to work in real time. In that case, we may not have the time to let our computer churn through a million possible scenarios, and having a formula to calculate (or quickly approximate) the quantity we need would be our only option. In reality, calculations and simulations can reinforce each other.  After all, we started with some quick sketches, and for a larger problem we might iterate on these stages many times: start at the “drawing board,” code up and run some simulations, go back to the drawing board to ask new questions, modify code, etc.

So the next time you see a problem that you're not sure how to calculate (or perhaps just don't want to calculate), see if you can simulate! And what's more, simulate with pride, knowing that you're taking advantage of one of the most powerful approaches in the data scientist's tool belt.
