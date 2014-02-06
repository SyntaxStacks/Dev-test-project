#! /usr/bin/python

import unittest
from reading import Reading
from measurements import Measurements

class TestMeasurements(unittest.TestCase):

    def setUp(self):
        self.inputFileName = "input.txt"

        mockReading1 = Reading(6.0, 8.0, 5.0)
        mockReading2 = Reading(0.0, 0.0, 5.0)
        self.measurements = [mockReading1, mockReading2]

    # TODO: replace this test with a validation of the input file schema
    # def testReadFile(self):
    #     expectedResult = "6.0 8.0 5.0\n0.0 0.0 5.0\n" # this is a FRAGILE test
    #     inputFile = open(self.inputFileName)
    #     result = inputFile.read(self.inputFileName)
    #     self.assertEqual(expectedResult, result)

    def testReadMeasurements(self):
        myMeasurements = Measurements()
        myMeasurements.readMeasurementsFile(self.inputFileName)

        self.assertEqual(2, len(myMeasurements.measurements))

    def testReadMeasurementsException(self):
        someBadFile = "doesNotExist.txt"
        myMeasurements = Measurements()
        self.assertRaises(Exception, myMeasurements.readMeasurementsFile, someBadFile)


if __name__ == '__main__':
    unittest.main()
