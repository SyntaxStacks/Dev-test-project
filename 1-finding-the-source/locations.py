class Locations():
    def __init__(self):
        self.locations = []

    def addLocation(self, location):
        if location not in self.locations:
            self.locations.append(location)

    def cleanUpLocations(self):
        pass
        #TODO: remove all but the single point that all circles go through

    def __repl__(self):
        print("made it to printLocations")
        if not self.locations:
            print("Unable to determine location from current measurement data.  Try adding more measurements!")
        print("{} {}",format(location.x, location.y))