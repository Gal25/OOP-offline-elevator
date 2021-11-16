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


def calc(call: Calls):
    return find_optimal_elev(call)


def find_optimal_elev(call: Calls):
    close_elev = None
    min_time = float('inf')
    for elev in listElev:
        find_direction(elev, elev.get_curr_floor(), call.get_src())
        arrival_src_time = elev.calc_elevator(elev.get_curr_floor(), call.get_src())
        find_direction(elev, call.get_src(), call.get_dest())
        arrival_dest_time = elev.calc_elevator(call.get_src(), call.get_dest())
        total_time = arrival_src_time + arrival_dest_time
        # print(total_time)
        # print(min_time)
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


# -----------------------------------------------------------------------------

# read from the csv

def read_csv(file: str) -> list:
    list_csv = []
    with open(file, newline='') as csv_list:
        csv_reader = csv.reader(csv_list)
        for row in csv_reader:
            c = Calls(row[1], row[2], row[3])
            # print(c)
            list_csv.append(c)
        # for val in listCalls:
        #     print(val.toString())
    return list_csv


# list back to file

def write_csv(file: str, new_list: list) -> None:  # new_list = calls (speed,
    # print(new_list)
    with open(file, 'w') as csv_file:
        for i in new_list:
            csv_file.write(i + '\n')


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
            # elevator = Elevator(**elev)
            building.add_elev(elevator)
        return building


BUILDING = sys.argv[1]
CALLS = sys.argv[2]
OUTPUT = 'Allocation.csv' #sys.argv[3]


def call_to_string(call, elev: int):
    call_dict = call.call_to_dict()
    return f"Elevator call,{call_dict.get('time')},{call_dict.get('src')},{call_dict.get('dest')},0,{elev}"


def main():
    global listElev

    b = read_json(BUILDING)
    listElev = b.get_elev()
    expected_calls = []
    calls = read_csv(CALLS)
    # print(os.getcwd())
    if len(listElev) == 0:
        print("There is no elevators in this building!")
    elif len(listElev) == 1:
        for call in calls:
            # call.set_elev(listElev[0])
            elevator = calc(call)
            expected_calls.append(call_to_string(call, elevator.get_id()))
        write_csv(OUTPUT, expected_calls)  # Calc_B.csv
        return

    for call in calls:
        # call.set_elev(calc(call))

        elevator = calc(call)
        # print(elevator.get_id())
        expected_calls.append(call_to_string(call, elevator.get_id()))
        for i in listElev:
            if i.get_id() == elevator.get_id():
                i.set_curr_floor(call.get_dest())

    #     call[5] = calc(call).get_id()
    #     print(call)
    write_csv(OUTPUT, expected_calls)


if __name__ == '__main__':
    main()
