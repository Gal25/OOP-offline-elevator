import Elevator

class Building:

    def __init__(self, minFloor, maxFloor) -> None:
        self.minFloor = int(minFloor)
        self.maxFloor = int(maxFloor)
        self.elevators = []

    def getminFloor(self):
        return self.minFloor

    def setminFloor(self, minFloor):
        self.minFloor = minFloor

    def getmaxFloor(self):
        return self.maxFloor

    def setmaxFloor(self, maxFloor):
        self.maxFloor = maxFloor


    def getEl(self):
        return self.elevators


    def setEl(self, elev: dict):
        self.elevators = elev

    #add the elevators to the list num of elevators
    def addEl(self, elev: Elevator):
        self.elevators.append(elev)

    def toString(self):
        str2 = ""

        for x in self.elevators:
            str2 += "{"
            str2 += "{},\n".format(x.toString())
            str2 += "}"
        str = "minFloor = {}, maxFloor = {}, numElevators = {},\n elevators = \n{}".format(
            self.minFloor, self.maxFloor, len(self.elevators), str2)
        return str