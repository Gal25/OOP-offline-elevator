# OOP-Ex1
This project is an assignment in an object-oriented course at Ariel University.
The purpose of the task is to find an optimal elevator to solve the offline-elevator problem.
The challenge is:
by given a call to the elevator from the source floor to the destination floor - the algorithm will want to embed the index of the elevator that will reduce the arrival time to a minimum. In general, upon receipt of a file of Calls and Buildings, we would like to run the algorithm on a the Building file, and in each case we will assign the ultimate elevator to each call that will ultimately give the average waiting time as low as possible.
In this solution to the elevator problem, we got a json file defined as a building as well as a csv file defined as a total calls.
The purpose of the algorithm is to assign the fastest elevator to the task. The way of realization is:

By definition the calls appear to be arranged chronologically, from the fastest call to the slowest call of the simulator. Indeed the algorithm revolves around the use of running time data and the speed of each elevator.

We will first note how the elevator works as given to us-
The elevator goes up and performs all the calls that are in its vicinity, then the elevator goes down to the bottom and again again performs the calls that are in its vicinity.

In case that there is one elevator:

We will built one list for all the readings of the elevator.
Each cell of the list will be defined according to the source and destination of the call, the order of the nodes in the list will be defined according to the order of the calls times received in advance (offline-elevator).

In case there is more than one elevator:

Adjust the call to the elevator according to the fastest elevator.
Since this is an OFFLINE case of the placement of the calls to the elevators, the beginning of the algorithm- the elevators are in LEVEL mode,in the zero floor of the building. The algorithm will call the fastest elevator, on first call, becuase without any prior thinking the all elevators start from the same floor.
Because we are given file of Call - there are call times, so we will work in the same chronological order of the arrival of the calls each time.
The algorithm assigns to each call the optimal elevator for it by connecting the variables:
* Calculate the time it takes for the elevator to get from its current floor in the building to the sorce floor of the given call.
* Calculate the time it takes for the elevator to get from the source floor of the call to the destination floor of that call.

Selectong the best choice - by comparing times of the elevators and choosing the fast elevator for the same call.
In calculating the elevator times we include the opening and closing times of the doors, acceleration and deceleration times in each elevator, and the division of the elevator speed according to the number of floors in the call are taken into account.
In addition, there is a reference to the direction of the elevator and adjusting the direction of the call to the direction of the elevator - in every time it takes the elevator to reach the destination (or the reading source or the reading destination) we will first want to check the direction of the elevator.

# External info:
* https://www.geeksforgeeks.org/fcfs-disk-scheduling-algorithms/
* http://www.intertent.co.il/2011/07/elevator-algorithm.html
* https://github.com/mshang/python-elevator-challenge

