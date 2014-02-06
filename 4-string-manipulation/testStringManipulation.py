#!/usr/bin/python

import unittest
import stringmanipulation

class TestStringManipulation(unittest.TestCase):
    def testRemovesAllSpaces(self):
        startingInput = "a b c d e f"
        expectedResult = "abcdef"
        result = stringmanipulation.compactSpacesAndDupes(startingInput)
        self.assertEqual(expectedResult, result)

    def testRemovesDuplicateNeighboringCharacters(self):
        startingInput = "abbbcccddeffgggf"
        expectedResult = "abcdefgf"
        result = stringmanipulation.compactSpacesAndDupes(startingInput)
        self.assertEqual(expectedResult, result)

    def testRemovesDuplicateNeighboringCharactersWithSpaces(self):
        startingInput = "ab b b c c cd defgg gf"
        expectedResult = "abcdefgf"
        result = stringmanipulation.compactSpacesAndDupes(startingInput)
        self.assertEqual(expectedResult, result)

    def testProvidedExample(self):
        startingInput = "abb cddpddef gh"
        expectedResult = "abcdpdefgh"
        result = stringmanipulation.compactSpacesAndDupes(startingInput)
        self.assertEqual(expectedResult, result)

    def testNonAlphaCharacters(self):
        startingInput = "_ . . ^ ^ A a 1   "
        expectedResult = "_.^Aa1"
        result = stringmanipulation.compactSpacesAndDupes(startingInput)
        self.assertEqual(expectedResult, result)

    def testLoadInputFromFile(self):
        inputFileName = "input.txt"
        expectedResult = "abb cddpddef gh\n"
        result = stringmanipulation.loadInputFromFile(inputFileName)
        self.assertEqual(expectedResult, result)

    def testMain(self):
        inputFileName = "input.txt"
        expectedResult = "abcdpdefgh"
        result = stringmanipulation.main(inputFileName)
        self.assertEqual(expectedResult, result)

if __name__ == '__main__':
    unittest.main()
