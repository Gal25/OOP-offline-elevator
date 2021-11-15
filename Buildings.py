import Elevator


class Building:

    def __init__(self, min_floor, max_floor) -> None:
        self.min_floor = int(min_floor)
        self.max_floor = int(max_floor)
        self.elevators = []

    # Getters & Setters

    def get_min_floor(self):
        return self.min_floor

    def set_min_floor(self, min_floor):
        self.min_floor = min_floor

    def get_max_floor(self):
        return self.max_floor

    def set_max_floor(self, max_floor):
        self.max_floor = max_floor

    def get_elev(self):
        return self.elevators

    def set_elev(self, elev: dict):
        self.elevators = elev

    def add_elev(self, elev: Elevator):
        self.elevators.append(elev)

    def to_string(self):
        str2 = ""
        for x in self.elevators:
            str2 += "{"
            str2 += "{},\n".format(x.toString())
            str2 += "}"
        string = "min_floor = {}, max_floor = {}, numElevators = {},\n elevators = \n{}".format(
            self.min_floor, self.max_floor, len(self.elevators), str2)
        return string
