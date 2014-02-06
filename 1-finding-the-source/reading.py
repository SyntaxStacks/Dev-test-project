class Reading():
    def __init__(self, x, y, distance):
        self.x = float(x)
        self.y = float(y)
        self.distance = float(distance)

    def __repr__(self):
    	return '"x:{}, y:{}, distance:{}"'.format(self.x, self.y, self.distance)
