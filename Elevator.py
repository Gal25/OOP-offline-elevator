import numpy as np
# from Building import Building


class Elevator:

    def __init__(self, _id, min_floor, max_floor, speed, close_time, open_time, start_time, stop_time) -> None:
        self.id = int(_id)
        self.min_floor = int(min_floor)
        self.max_floor = int(max_floor)
        self.speed = float(speed)
        self.close_time = float(close_time)
        self.open_time = float(open_time)
        self.start_time = float(start_time)
        self.stop_time = float(stop_time)
        self.curr_floor = int(0)
        self.direction_el = int(0)  # 1 - up, -1 - down 0 - init
        self.available_elev = int(0)  # 1 not available, 0 - available

    # Getters & Setters

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_min_floor(self):
        return self.min_floor

    def set_min_floor(self, min_floor):
        self.min_floor = min_floor

    def get_max_floor(self):
        return self.max_floor

    def set_max_floor(self, max_floor):
        self.max_floor = max_floor

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_close_time(self):
        return self.close_time

    def set_close_time(self, close_time):
        self.close_time = close_time

    def get_open_time(self):
        return self.open_time

    def set_open_time(self, open_time):
        self.open_time = open_time

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_stop_time(self):
        return self.stop_time

    def set_stop_time(self, stop_time):
        self.stop_time = stop_time

    def get_curr_floor(self):
        return self.curr_floor

    def set_curr_floor(self, curr_floor):
        self.curr_floor = curr_floor

    def get_direction_el(self):
        return self.direction_el

    def set_direction_el(self, direction_el):
        self.direction_el = direction_el

    def get_available_elev(self):
        return self.available_elev

    def set_available_elev(self, available_elev):
        self.available_elev = available_elev

    # Calculate the whole time the elevator goes between src and dest
    def calc_elevator(self, src, dest):
        """
        This function measures the time the elevator operates according to each call.
        The calculation: according to the source floor and its time to reach the target floor, taking into account the
        elevator speed, stopping and acceleration times, opening and closing doors.
        :param src: src floor - of the specific call
        :param dest: destination floor - of the specific call
        :return: elevator operation time
        """
        i = 0
        if src == dest:
            return 0
        elif (src <= 0 and dest > 0) or (src > 0 and dest <= 0):
            i = 1
        val = abs(dest - src) + i
        val *= self.speed
        val += self.open_time + self.close_time + self.stop_time + self.start_time
        # print("val = {}".format(val))
        return val

    # def __repr__(self):
    #     return "_id = {}, min_floor = {}, max_floor = {}, speed = {}, close_time = {}, open_time = {}, start_time = {" \
    #              "}, stop_time = {}, curr_floor = {}, direction_el = {}, available_elev = {}".format(self.id,
    #                                                                                                  self.min_floor,
    #                                                                                                  self.max_floor,
    #                                                                                                  self.speed,
    #                                                                                                  self.close_time,
    #                                                                                                  self.open_time,
    #                                                                                                  self.start_time,
    #                                                                                                  self.stop_time,
    #                                                                                                  self.curr_floor,
    #                                                                                                  self.direction_el,
    #                                                                                                  self.available_elev)


def matrix_el(check_building) -> None:
    """
    This function defines the Adjacency Matrix which we will work with.The matrix:
    A square matrix, will be the size of the building. Calculation - the difference between the minimum floor and the
    maximum plus 1 (= zero floor).
    The rows will form the src floors The columns will form the dest floors according to each call.
    :param check_building: the building to have the size of the matrix
    #:param elev_matrix: any elevator from the Elevators list
    :return: A matrix that constitutes all the running times of the elevator for all possible calls
            (get a top triangular matrix)
    """
    building_max_floor = check_building.get_max_floor()
    building_min_floor = check_building.get_min_floor()
    length = abs(building_max_floor - building_min_floor) + 1
    elev_matrix = np.matrix(length)
    for i in range(len(elev_matrix)):
        for j in range(len(elev_matrix[0])):
            if i == j:
                elev_matrix[i][j] = 0
                # will be zero because the src floor and the dest floor are the same and there no movement
            elif i < j:
                elev_matrix[i][j] = elev_matrix.calc_elevator(i, j)
            else:
                pass
