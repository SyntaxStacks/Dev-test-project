#! /usr/bin/python

import unittest
from locationcalculator import LocationCalculator
from reading import Reading

class TestLocationCalculator(unittest.TestCase):
    def setUp(self):
        mockReading1 = Reading(6.0, 8.0, 5.0)
        mockReading2 = Reading(0.0, 0.0, 5.0)
        self.measurements = [mockReading1, mockReading2]

    def testFindDistanceBetweenPoints(self):
       locator = LocationCalculator(self.measurements) 
       result = locator.calculateDistanceBetweenMeasurements()
       expectedResult = 10;
       self.assertEqual(expectedResult, result)

    def testValidateMeasurementsForLocationLookup(self):
       locator = LocationCalculator(self.measurements) 
       result = locator.validateMeasurementsForLocationLookup()
       expectedResult = True
       self.assertEqual(expectedResult, result)

    def testGetLocationCoordinates(self):
        locator = LocationCalculator(self.measurements)
        locations = locator.findLocation()

    def testInvalidCoords(self):
        mockReading1 = Reading(6.0, 8.0, 20.0)
        mockReading2 = Reading(0.0, 0.0, 5.0)
        measurements = [mockReading1, mockReading2]

        locator = LocationCalculator(measurements)
        result = locator.validateMeasurementsForLocationLookup()
        expectedResult = False 
        self.assertEqual(expectedResult, result)

if __name__ == '__main__':
    unittest.main()