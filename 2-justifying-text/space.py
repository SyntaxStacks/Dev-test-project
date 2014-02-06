class Space():
    def __init__(self, place, location):
        self.place = place 
        self.location = location

    def __repr__(self):
        return"place: {} location: {}".format(self.place, self.location) 
