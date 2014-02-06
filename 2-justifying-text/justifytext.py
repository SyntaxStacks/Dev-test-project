#! /usr/bin/python

import math
from sys import argv
from justifiedtext import JustifiedText  

class TextReader():
    def __init__(self, fileName):
        self.fileName = fileName
        self.lineCount = 0

    def readText(self):
        with open(self.fileName) as inputFile:
            for line in inputFile:
                self.handleLine(line)
            self.justifiedText.finalizeJustify()

    def handleLine(self, line):
        try: 
            if self.lineCount < 1:
                self.columnSize = line
                self.justifiedText = JustifiedText(self.columnSize)
            else:
                words = line.split(' ')
                for word in words:
                    self.justifiedText.addWord(word)
            self.lineCount += 1

        except Exception, e:
            raise Exception("Unable to read input file.")

def main():
    inputFileName = getFileName()
    myTextReader = TextReader(inputFileName)
    myTextReader.readText()
    myTextReader.justifiedText.printJustifiedText()


def getFileName():
    try:
        script, fileName = argv
        return fileName
    except Exception, e:
        raise Exception("Please provide a file name.")


if __name__ == '__main__':
    try:
        main()
    except Exception(), e:
        print(e)

