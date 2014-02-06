#! /usr/bin/python

import unittest
from findsource import Finder
from reading import Reading


class TestFindSource(unittest.TestCase):

    def setUp(self):
        self.inputFileName = "input.txt"

        mockReading1 = Reading(6.0, 8.0, 5.0)
        mockReading2 = Reading(0.0, 0.0, 5.0)
        self.measurements = [mockReading1, mockReading2]

        # mockFinder = Finder()
        # mockFinder.measurements = [Measurement(6.0, 8.0, 5.0), Measurement(0.0, 0.0, 5.0)]
        # self.assertEqual(len(mockFinder.measurements), len(self.myFinder.measurements))

    # def testFindOriginFromFileInput(self):
    #     inputFileName = "input.txt"
    #     datapoints = findsource.readDataPoints(self.inputFileName)
    #     origin = findsource.calculateOrigin(datapoints)

if __name__ == '__main__':
    unittest.main()
