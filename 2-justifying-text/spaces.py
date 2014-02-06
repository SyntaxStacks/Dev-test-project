from space import Space
import math

class Spaces():
    def __init__(self, line):
        self.line = line
        self.spaces = []

    def catalogSpaces(self):
        place = 0 
        for i in range(0, len(self.line)):
            if self.line[i] == ' ':
                place += 1
                location = i
                self.spaces.append(Space(place, location))
        # print("spaces found: " + str(len(self.spaces)))
                

    def getMiddleSpacePlace(self):
        # print("length of total spaces: " + str(len(self.spaces)))
        middleSpace = int(math.ceil(len(self.spaces) / 2))
        # print("middleSpace: " + str(middleSpace))
        return middleSpace

    def getLocation(self, place):
        # print("place" + str(place))
        return self.spaces[place].location
