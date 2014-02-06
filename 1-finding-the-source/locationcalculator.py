import math
from location import Location
from measurements import Measurements
from reading import Reading

class LocationCalculator():
    def __init__(self, measurements):
        self.c1, self.c2 = measurements
        self.a1 = self.c1.x
        self.a2 = self.c2.x
        self.b1 = self.c1.y
        self.b2 = self.c2.y
        self.r1 = self.c1.distance
        self.r2 = self.c2.distance
        self.calculateDistanceBetweenMeasurements()

    def calculateDistanceBetweenMeasurements(self):
        self.measurementDistance = math.sqrt((self.a2 - self.a1) * (self.a2 - self.a1) + (self.b2 - self.b1) * (self.b2 - self.b1))

    def validateMeasurementsForLocationLookup(self):
        pointsRadiusSum = self.r1 + self.r2
        pointsRadiusDifference = math.fabs(self.r1 - self.r2)

        validPoints = (pointsRadiusSum >= self.measurementDistance and 
            self.measurementDistance >= pointsRadiusDifference)
        return validPoints

    def findLocation(self):
        valid = self.validateMeasurementsForLocationLookup()
        if not valid:
            raise Exception("Invalid measurements")

        xAverage = (self.a1 + self.a2) / 2
        yAverage = (self.b1 + self.b2) / 2

        xDifference = (self.a2 - self.a1)
        yDifference = (self.b2 - self.a2)

        squaredRadiusDifference = (math.pow(self.r1, 2) - math.pow(self.r2, 2))
        twiceMeasurementDistanceSquared = 2 * math.pow(self.measurementDistance, 2)

        x = xAverage + xDifference * squaredRadiusDifference / twiceMeasurementDistanceSquared
        y = yAverage + yDifference * squaredRadiusDifference / twiceMeasurementDistanceSquared

        newLocationFound = Location(x, y)

        return newLocationFound

