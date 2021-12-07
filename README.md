# Repo for coding questions solutions
## Solution 1
### Premise:
    This is the solution to find out how many times a robot passes by the same vector on an unknown sized grid.

### Solution:
    The start of the code works as a generator for the path that the robot takes,
    since we are not getting inputs from the exam/test environment.
    
    The robot moves are expressed by ^ up, v down, < left, > right.

    We then start a dictionary to keep track of the robot visited locations as
    well as starting a list to keep track of the robot current location.

    Now we just go and for each direction that the robot moves to in route we add
    or subtract to our axis depending on said direction.

    ^ will increment Y in 1
    v will decrease Y in 1
    > will increment X in 1
    < will decrease X in 1

    After calculating the current location we will check for it in the dictionary (walked) 
    if it's present we'll increase the amount of times we've visited that location by 1 if not we'll
     initialize it with the value of 1.

    We then create another list with all the values from walked and get the maximum value within said list
    to retrieve the number of times the robot revisited a location.

    The question didn't ask for said location value, or even if multiple locations where the answer, 
    it just asked to keep track of revisits and output the max number possible givin a route.

    