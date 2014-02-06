#!/usr/bin/python

from sys import argv
import re

def compactSpacesAndDupes(targetString):
    '''
    (.) match any single character
    (?= start positive lookahead
        (\s)? optionally match spaces
        \1 match the single character from the first reference
    ) close positive lookahead
    | or condition
    \s match space
    '''
    patternFilterDupesAndSpaces = r'(.)(?=(\s+)?\1)|\s'
    filteredInput = re.sub(patternFilterDupesAndSpaces, '', targetString)
    return filteredInput

def loadInputFromFile(fileName):
    inputFile = open(fileName)
    fileInputText = inputFile.read()
    return fileInputText

def main(fileName):
    inputString = loadInputFromFile(fileName)
    compactedResult = compactSpacesAndDupes(inputString)
    return compactedResult

if __name__ == "__main__":
    script, fileName = argv
    result = main(fileName)
    print(result)
