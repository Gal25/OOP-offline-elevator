import json
import csv
import sys
import os.path
from Calls import Calls
from Buildings import Building
from Elevator import Elevator
import numpy as np

# 0 -> 4
# 3 -> 0

# 0 -> 4

#the list of the calls
listCalls = []
#the list of the elevators
listElev = []
#the length of the building
length = 0


#calclute the total time
def calc(b: Building):
        length = abs(b.getmaxFloor() - b.getminFloor()) + 1
        print("lengthB = {}".format(length))
        min = b.getminFloor()
        print("min = {}".format(min))
        for floor in range(length):
            # result = length  + x + 1
            row = length + floor + 1
            col = length + (floor + 1) + 1
            srcFloor = row - length - 1
            destFloor = col - length - 1
            # print(" index of row is : lengthB + floor = {} + {} = {}".format(length, floor, (row)))
            # print(" index of col is : lengthB + floor = {} + {} = {}".format(length, floor + 1, (col)))
            # print(" row - length - 1 = {} - 1 - {} = {}".format(row, length, (srcFloor)))
            # print(" col - length - 1 = {} - 1 - {} = {}\n".format(col, length, (destFloor)))
        # c1 = listCalls[0]
        # c2 = listCalls[1]
        # c3 = listCalls[2]
        # for call in listCalls:
        # print(c1.get_src())
        # print(c1.get_dst())
        # c1L = c1.calc()
        # c2L = c2.calc()
        # c3L = c3.calc()
        # print("c1 = {}".format(c1.toString()))
        # print("c2 = {}".format(c2.toString()))
        # print("c3 = {}".format(c3.toString()))
        e1 = b.getEl()[0]
        # oldtime = 0
        # print("e1 = {} ".format(e1.toString()))

        #run on the calls and the numbers of elevators in the buliding
        for c in listCalls:
            for e in b.elevators:
                print("index {}".format(length - abs(min) + c.get_src()))
                print("c = {} ".format(c.toString()))

                time = e.calc(e.get_curr_floor(), c.get_src())

                # what is the direction of the elevator
                if e.get_curr_floor() > c.get_src():
                    e.set_dirc_el(-1)
                elif e.get_curr_floor() < c.get_src():
                    e.set_dirc_el(1)

                time += e.calc(c.get_src(), c.get_dst())

                if e.get_curr_floor() > c.get_src():
                    e.set_dirc_el(-1)
                elif e.get_curr_floor() < c.get_src():
                    e.set_dirc_el(1)

                # init the current floor by the destination of the last call
                e1.set_curr_floor(c.get_dst())

                # oldtime += time
                print(" time = {}".format(time))
                print("e = {} ".format(e.toString()))

                #check the best elev to the call
                theBestElev(e,c)
                return e.getID


#check if one elevator (one martix) time to the dest is less then the other if, if yes allocate this elevator
def theBestElev(e:Elevator, c:Calls):
        length = abs(b.getmaxFloor() - b.getminFloor()) + 1
        for floor in range(length):
            row = length + floor + 1
            col = length + (floor + 1) + 1
            srcFloor = row - length - 1
            destFloor = col - length - 1
            print("dest = {} ".format(destFloor))
            check_e = matrix_el(e, c)
            # check_e1 = matrix_el((e1 + i),c)
            temp = 0
            # temp = check_e1[srcFloor][destFloor]
            if (check_e[srcFloor][destFloor] < temp):
                temp = check_e[srcFloor][destFloor]
                print("ID = {}", e.getID)
                return e.getID

#put in the matrix the elevators : the row and the col will be the num of the floors in the buliding.
#in the matrix the upper half will be the time between src floor and dest floor
#when the src=dest (diagnal matrix) the time will be 0
def matrix_el(e: Elevator, c : Calls) -> None:
        length = abs(b.maxFloor - b.minFloor) + 1
        for floor in range(length):
            # result = length  + x + 1
            row = length + floor + 1
            col = length + (floor + 1) + 1
            elev_matrix = np.matrix(length + 1)
            for i in range(len(elev_matrix)):
                for j in range(len(elev_matrix[0])):
                    if (i == j):
                        elev_matrix[i][j] = 0
                    elif (i < j):
                        elev_matrix[row][col] = elev_matrix.Elevator.calc(c.get_src(), c.get_dst())
                        print(elev_matrix)


        # print("c2 = {}".format(c2L))
        # print(c2.get_src())
        # print(c2.get_dst())

        # print(c1.toString())
        # print(c2.toString())


    # length =(b.maxFloor - b.minFloor +1)
    # mat = np.matrix(length)
    # print(mat)
    # print("length = {}".format(length))
    # elev1 = b.elevators[1]
    # elev0 = b.elevators[0]

    # print("elev 0 = {}".format(elev0.calc(-1,10)))
    # print("elev 1 = {}".format(elev1.calc(-1,10)))

    # def comper_time()


# def fastest_elevator(elev: Elevator) -> int:
#         ans = 0
#         temp = building_data["_elevators"].get(0).speed
#         for i in len(building_data["_elevators"]):
#             if building_data["_elevators"].get(i).speed > temp:
#                 temp = building_data["_elevators"].get(i).speed
#             ans = i
#         return ans


# read from the csv
def read_csv(file: str) -> list:
        list_csv = []
        with open(file, newline='') as csv_list:
            csv_reader = csv.reader(csv_list)
            for row in csv_reader:
                c = Calls(row[1], row[2], row[3])
                listCalls.append(c)
            # for val in listCalls:
            #     print(val.toString())
        return list_csv


# list back to file
def write_csv(file: str, new_list: list) -> None:
        with open(file, 'w+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(new_list)


# read Json to Dict
def read_json(file: str) -> Building:
        with open(file) as json_file:
            json_data = json.load(json_file)
            _minFloor = int(json_data['_minFloor'])
            _maxFloor = int(json_data['_maxFloor'])
            length = _maxFloor - _minFloor + 1
            b = Building(_minFloor, _maxFloor)
            for e in json_data['_elevators']:
                _id = e["_id"]
                _minFloor = e["_minFloor"]
                _maxFloor = e["_maxFloor"]
                _speed = e["_speed"]
                _closeTime = e["_closeTime"]
                _openTime = e["_openTime"]
                _startTime = e["_startTime"]
                _stopTime = e["_stopTime"]
                elev = Elevator(_id, _minFloor, _maxFloor, _speed, _closeTime, _openTime, _startTime, _stopTime)
                b.addEl(elev)
            return b

        return json_data

#Receive the building files and calls
BUILDING = os.path.join(sys.argv[1])
CALLS = os.path.join(sys.argv[2])
OUTPUT = 'Allocation.csv'

if __name__ == '__main__':
        b = building_data = read_json(BUILDING)
        calls = read_csv(CALLS)
        print(b.toString())
        calc(b)

# finish
# write_csv(OUTPUT, calls)

