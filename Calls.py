class Calls:

    def __init__(self, time, src, dest) -> None:
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        if src > dest:
            self.direction_el = int(-1)
        elif src < dest:
            self.direction_el = int(1)
        self.Elev = int(-1)

    # Getters & Setters

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_src(self):
        return self.src

    def set_src(self, src):
        self.src = src

    def get_dest(self):
        return self.dest

    def set_dest(self, dest):
        self.dest = dest

    def get_elev(self):
        return self.Elev

    def set_elev(self, elev):
        self.Elev = elev

    def get_direction_el(self):
        return self.direction_el

    def set_direction_el(self, direction_el):
        self.direction_el = direction_el

    def __repr__(self):
        return "time = {}, get_src = {}, get_dest = {}, Elev = {}".format(
            self.time, self.src, self.dest, self.Elev)

    def call_to_dict(self):
        return {
            'time': self.time,
            'src': self.src,
            'dest': self.dest,
            'elev': self.Elev
        }
