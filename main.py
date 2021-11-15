import json
import csv
import sys
import os.path
from Calls import Calls
from Building import Building
from Elevator import Elevator
import numpy as np

listCalls = []
listElev = []
length = 0


def calc(building: Building):
    check_base_floor = abs(0 - building.get_min_floor()) + 1

    # -------------------------------------------------------------------------------------------
    """
    The calculation for the conversion of the source floor and the destination of the call to the correct
    position of the index in the matrix.
    The formula to get the index of the src and the dest in the mat:
          row (src) = abs(0 - min floor of the building) + src_of_the_call + 1
          col (dest) = abs(0 - min floor of the building) + dest_of_the_call + 1
    The formula to get the src and the dest floor from the index in the matrix:
          src_floor = row - length - 1
          dest_floor = col - length - 1
    """
    # an example to run on 11 floors

    # row = check_base_floor + floor + 1
    # col = check_base_floor + floor + 1
    # src_floor = row - length - 1
    # dest_floor = col - length - 1
    # print(" index of row is : lengthB + floor = {} + {} = {}".format(length, floor, row))
    # print(" index of col is : lengthB + floor = {} + {} = {}".format(length, floor + 1, col))
    # print(" row - length - 1 = {} - 1 - {} = {}".format(row, length, src_floor))
    # print(" col - length - 1 = {} - 1 - {} = {}\n".format(col, length, dest_floor))
    # -------------------------------------------------------------------------------------------

    oldtime = 0

    """
    Start checking the optimal elevator to do the call - a comparison made by the elevator speed in this call
    Start loop on the Calls list and in each call, then start to check on the each elevator (in the building)
    The optimal choice is the calculation of the elevator that performs the call in the shortest time.  
    """
     for call in listCalls:
        best_elev = find_optimal_elev(call)
        yield best_elev
    # for elevator in listElev:
    #      print("index {}".format(check_length - abs(min) + call.get_src()))
    #      print("call = {} ".format(call.to_string()))
    #
    #      time = elevator.calc(elevator.get_curr_floor(), call.get_src())
    #
    #      # what is the direction of the elevator
    #      if elevator.get_curr_floor() > call.get_src():
    #          elevator.set_direction_el(-1)
    #      elif elevator.get_curr_floor() < call.get_src():
    #          elevator.set_direction_el(1)
    #
    #      time += elevator.calc(call.get_src(), call.get_dest())
    #
    #      # what is the direction of the elevator after the elevator go to the dest floor???
    #      if elevator.get_curr_floor() > call.get_src():
    #          elevator.set_direction_el(-1)
    #      elif elevator.get_curr_floor() < call.get_src():
    #          elevator.set_direction_el(1)
    #
    #      # init the current floor by the destination of the last call
    #      elevator.set_curr_floor(call.get_dest)
    #
    #      # old_time += time
    #      print(" time = {}".format(time))
    #      print("e1 = {} ".format(e2.toString()))

    # -------------------------------------------------------------
    # check_e = Elevator.matrix_el(e, c)
    # check_e1 = Elevator.matrix_el((e + 1), c)
    #
    # for i in Elevator.matrix_el(e, c).size():
    #     Elevator.matrix_el(e, c)
    #     Elevator.matrix_el((e + i), c)
    #
    #     temp = check_e1[c.get_src][c.get_dst]
    #     if check_e[c.row][c.col] < temp:
    #         temp = check_e[c.row][c.col]
    #         return e.getID

    # elev = b.elevators


def find_optimal_elev(call: Calls):
    close_elev = None
    min_time = float('inf')
    for elev in listElev:
        find_direction(elev, elev.get_curr_floor(), call.get_src())
        arrival_src_time = elev.calc(elev.get_curr_floor(), call.get_src())
        find_direction(elev, call.get_src(), call.get_dest())
        arrival_dest_time = elev.calc(call.get_src(), call.get_dest())
        total_time = arrival_src_time + arrival_dest_time
        if total_time < min_time:
            min_time = total_time
            close_elev = elev
    return close_elev


# init the direction of the elevator per call
def find_direction(elev, src, dest):
    if src > dest:
        elev.set_direction_el(-1)
    elif src < dest:
        elev.set_direction_el(1)


# def fastest_elevator(elev: Elevator) -> int:
#     ans = 0
#     temp = building_data["_elevators"].get(0).speed
#     for i in len(building_data["_elevators"]):
#         if building_data["_elevators"].get(i).speed > temp:
#             temp = building_data["_elevators"].get(i).speed
#         ans = i
#     return ans
# -----------------------------------------------------------------------------

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
        check_length = _maxFloor - _minFloor + 1
        building = Building(_minFloor, _maxFloor)
        for elev in json_data['_elevators']:
            _id = elev["_id"]
            _minFloor = elev["_minFloor"]
            _maxFloor = elev["_maxFloor"]
            _speed = elev["_speed"]
            _closeTime = elev["_closeTime"]
            _openTime = elev["_openTime"]
            _startTime = elev["_startTime"]
            _stopTime = elev["_stopTime"]
            elevator = Elevator(_id, _minFloor, _maxFloor, _speed, _closeTime, _openTime, _startTime, _stopTime)
            # print(elevator.to_string())
            building.add_elev(elevator)
        return building

    return json_data


BUILDING = os.path.join(sys.argv[1])
CALLS = os.path.join(sys.argv[2])
OUTPUT = 'Allocation.csv'

if __name__ == '__main__':
    b = building_data = read_json(BUILDING)
    calls = read_csv(CALLS)
    # print(b)
    # calc(b)
    # find_optimal_elev(calls)
    for index in range(len(calls)):
        call = calls[index]
        # call[5] = calc
    write_csv(OUTPUT, calls)
