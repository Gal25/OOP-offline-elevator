# OOP-Ex1
This project is an assignment in an object-oriented course at Ariel University.
The purpose of the task is to find an optimal solution to the offline-elevator problem.
The challenge of the elevator problem is - given a call to the elevator from the source floor to the destination floor - the system will want to embed the elevator that will reduce the arrival time to a minimum. That is, more generally it is said that given a collection of lifts calls in time we would like to define an elevator placement strategy for calls that will minimize the total arrival time for all calls.
In this solution to the elevator problem we got a json file defined as a building as well as a csv file which we were a file containing the total calls.
The purpose of the algorithm is to assign the fastest elevator to the task. The way of realization is:

If there is one elevator –

One list was built for all the readings of the elevator.
Each cell of the list will be defined according to the source and destination of the reading, the order of the nodes in the list will be defined according to the order of the read times received in advance (offline- elevator).

First the elevator will approach the first compartment first since this is the first reading, we will examine whether its direction is ascending or descending. We will then go through the entire list i.e. all the readings and examine whether there are readings whose origin is included within the reading range of the current node, i.e. we will sort the list according to the reading source.
If there is a call that is covered within the elevator range, the overlapping calls will also be added to the route. If not, the elevator will leave the same readings on a temporary basis
Reading them.

If there is more than one elevator-

For ascending readings, a ListUp list is constructed.
For calls from elevators that are descending, a ListDown list is constructed.

Each cell of a list will be defined by source and destination, the order of the cells in the list will be defined by the order of read times.

ListUp:
The first elevator will be assigned to the first junction i.e. to the first reading. :
We will go through the entire list and examine whether there are readings whose origin is included within the reading range of the current node: if so, the elevator will attach to the track the reading of the current node.
If not, we will assign another elevator to read the current node.

ListDown:
The first elevator will be assigned to the first junction i.e. to the first reading.
We will go through the entire list and examine whether there are readings whose origin is included within the reading range of the current node: if so, the elevator will attach to the track the reading of the current node.
If not, we will assign another elevator to read the current node.

