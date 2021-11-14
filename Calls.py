class Calls:

    def __init__(self, time, src, dst) -> None:
        self.time = float(time)
        self.src = int(src)
        self.dst = int(dst)
        if src > dst:
            self.dirc_el = int(-1)
        elif src < dst:
            self.dirc_el = int(1)
        self.Elev = int(-1)

    def get_dirc_el(self):
        return self.dirc_el

    def set_dirc_el(self, dirc_el):
        self.dirc_el = dirc_el

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def calc(self):
        i = 0
        if (self.src == self.dst):
            return 0
        elif (self.src <= 0 and self.dst > 0) or (self.src > 0 and self.dst <= 0):
            i = 1
        val = abs(self.dst - self.src) + i
        return val

    def get_src(self):
        return self.src

    def set_src(self, src):
        self.src = src

    def get_dst(self):
        return self.dst

    def set_dst(self, dst):
        self.dst = dst

    def getElev(self):
        return self.Elev

    def setElev(self, elev):
        self.Elev = elev

    def toString(self) -> str:
        str = "time = {}, getSrc = {}, getDst = {}, Elev = {}".format(
            self.time, self.src, self.dst, self.Elev)
        return str