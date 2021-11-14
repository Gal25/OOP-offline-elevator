import numpy as np
from Calls import Calls


class Elevator:

    def __init__(self, _id, minFloor, maxFloor, speed, closeTime, openTime, startTime, stopTime) -> None:
        self.id = int(_id)
        self.minFloor = int(minFloor)
        self.maxFloor = int(maxFloor)
        self.speed = float(speed)
        self.closeTime = float(closeTime)
        self.openTime = float(openTime)
        self.startTime = float(startTime)
        self.stopTime = float(stopTime)
        self.curr_floor = int(0)
        self.dirc_el = int(0)  # 1 - up, -1 - down 0 - init
        self.available_elev = int(0)  # 1 not available, 0 - available

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def get_minFloor(self):
        return self.minFloor

    def set_minFloor(self, minFloor):
        self.minFloor = minFloor

    def get_maxFloor(self):
        return self.maxFloor

    def set_maxFloor(self, maxFloor):
        self.maxFloor = maxFloor

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_closeTime(self):
        return self.closeTime

    def set_closeTime(self, closeTime):
        self.closeTime = closeTime

    def get_openTime(self):
        return self.openTime

    def set_openTime(self, openTime):
        self.openTime = openTime

    def get_startTime(self):
        return self.startTime

    def set_startTime(self, startTime):
        self.startTime = startTime

    def get_stopTime(self):
        return self.stopTime

    def set_stopTime(self, stopTime):
        self.stopTime = stopTime

    def get_curr_floor(self):
        return self.curr_floor

    def set_curr_floor(self, curr_floor):
        self.curr_floor = curr_floor

    #the diraction of the elevator
    def get_dirc_el(self):
        return self.dirc_el

    def set_dirc_el(self, dirc_el):
        self.dirc_el = dirc_el

    #if the elevator is available
    def get_available_elev(self):
        return self.available_elev

    def set_vailable_elev(self, available_elev):
        self.available_elev = available_elev

    #this function takes the src and the dest of the call and calclute the time of the elev antil she end the call
    def calc(self, src, dest):
        i = 0
        if (src == dest):
            return 0

        #if the src and dest is one (-) and else (+) so we add 1 to the sum of floor becouse the floor 0
        elif (src <= 0 and dest > 0) or (src > 0 and dest <= 0):
            i = 1
        val = abs(dest - src) + i
        val *= self.speed
        val += self.openTime + self.closeTime + self.stopTime + self.startTime
        # print("val = {}".format(val))
        return val

    # def getminFloor(self):
    #     return self.minFloor
    #
    # def setminFloor(self, minFloor):
    #     self.minFloor = minFloor

    # b = Building

    # def matrix_el(self, e : Elevator) -> None:
    #     length = abs(self.maxFloor - self.minFloor) + 1
    #     elev_matrix = np.matrix().size = length + 1
    #     for i in range(len(elev_matrix)):
    #         for j in range(len(elev_matrix[0])):
    #             if (i == j):
    #                 elev_matrix[i][j] = 0
    #             elif (i < j):
    #                 elev_matrix[i][j] = elev_matrix.calc_elevator(c.get_src(), c.get_dst())

    def toString(self):
        str = "_id = {}, minFloor = {}, maxFloor = {}, speed = {}, closeTime = {}, openTime = {}, startTime = {" \
              "}, stopTime = {}, curr_floor = {}, dirc_el = {}, available_elev = {}".format(self.id,
                                                                                            self.minFloor,
                                                                                            self.maxFloor,
                                                                                            self.speed,
                                                                                            self.closeTime,
                                                                                            self.openTime,
                                                                                            self.startTime,
                                                                                            self.stopTime,
                                                                                            self.curr_floor,
                                                                                            self.dirc_el,
                                                                                            self.available_elev)
        return str
