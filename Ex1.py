import json
import csv
import sys
from Calls import Calls
from Building import Building
from Elevator import Elevator

listCalls = []
listElev = []
length = 0


def find_optimal_elev(call: Calls):
    """
    this function check the which is the optimal elevator to the call.
    first we check the direction of the elevator with the helper function 'find_direction',
    and then we calculate the time it will take for the elevator to get from the current floor to the src floor,
    then calculate the time that the elevator go to the dest floor from the src floor.
    after that we compare to each elevator in the building.

    :param call:
    :return: the optimal elevator
    """
    close_elev = None
    min_time = float('inf')
    total_time = 0
    for elev in listElev:
            if find_direction(elev, call.get_src(), call.get_dest()) == 1:

                if find_direction(elev, elev.get_curr_floor(), call.get_src()) == 1:
                    arrival_src_time = elev.calc_elevator(elev.get_curr_floor(), call.get_src())
                    arrival_dest_time = elev.calc_elevator(call.get_src(), call.get_dest())
                    total_time = arrival_src_time + arrival_dest_time

                elif find_direction(elev, elev.get_curr_floor(), call.get_src()) == -1:
                    arrival_src_time = elev.calc_elevator(elev.get_curr_floor(), call.get_src())
                    arrival_dest_time = elev.calc_elevator(call.get_src(), call.get_dest())
                    total_time = arrival_src_time + arrival_dest_time + ((abs(elev.get_min_floor() - elev.get_min_floor()))/elev.get_speed())

            elif find_direction(elev, call.get_src(), call.get_dest()) == -1:

                if find_direction(elev, elev.get_curr_floor(), call.get_src()) == -1:
                    arrival_src_time = elev.calc_elevator(elev.get_curr_floor(), call.get_src())
                    arrival_dest_time = elev.calc_elevator(call.get_src(), call.get_dest())
                    total_time = arrival_src_time + arrival_dest_time

                elif find_direction(elev, elev.get_curr_floor(), call.get_src()) == 1:
                    arrival_src_time = elev.calc_elevator(elev.get_curr_floor(), call.get_src())
                    arrival_dest_time = elev.calc_elevator(call.get_src(), call.get_dest())
                    total_time = arrival_src_time + arrival_dest_time + ((abs(elev.get_max_floor() - elev.get_min_floor()))/elev.get_speed())

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
            list_csv.append(c)
    return list_csv


# list back to file

def write_csv(file: str, new_list: list) -> None:  # new_list = calls (speed,
    with open(file, 'w') as csv_file:
        for i in new_list:
            csv_file.write(i + '\n')


# read Json to Dict

def read_json(file: str) -> Building:
    with open(file) as json_file:
        json_data = json.load(json_file)
        _minFloor = int(json_data['_minFloor'])
        _maxFloor = int(json_data['_maxFloor'])
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
            building.add_elev(elevator)
        return building


BUILDING = sys.argv[1]
CALLS = sys.argv[2]
OUTPUT = 'Allocation.csv'


def call_to_string(call, elev: int):
    call_dict = call.call_to_dict()
    return f"Elevator call,{call_dict.get('time')},{call_dict.get('src')},{call_dict.get('dest')},0,{elev}"


def main():
    global listElev

    b = read_json(BUILDING)
    listElev = b.get_elev()
    expected_calls = []
    calls = read_csv(CALLS)
    if len(listElev) == 0:
        print("There is no elevators in this building!")
    elif len(listElev) == 1:
        for call in calls:
            elevator = find_optimal_elev(call)
            expected_calls.append(call_to_string(call, elevator.get_id()))
        write_csv(OUTPUT, expected_calls)
        return

    for call in calls:
        elevator = find_optimal_elev(call)
        expected_calls.append(call_to_string(call, elevator.get_id()))
        for i in listElev:
            if i.get_id() == elevator.get_id():
                i.set_curr_floor(call.get_dest())
    write_csv(OUTPUT, expected_calls)


if __name__ == '__main__':
    main()
