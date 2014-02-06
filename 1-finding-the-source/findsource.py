#! /usr/bin/python

from sys import argv, exit
import math
import itertools
from reading import Reading 
from measurements import Measurements
from locations import Locations
from locationcalculator import LocationCalculator

class Finder():
	def __init__(self, measurements, locations):
		self.measurements = measurements
		self.locations = locations 

	def findLocations(self):
		'''
		Allow use of 2 or more measurements to locate origin.
		'''
		if len(self.measurements) <= 1:
			raise Exception("To find location, more than 1 measurement required.")

		combinations = itertools.combinations(self.measurements, 2)
		for measurementPair in combinations:
			try:
				locator = LocationCalculator(measurementPair)
				newLocation = locator.findLocation()
				self.locations.addLocation(newLocation)
			except Exception, e:
				continue
		self.locations.cleanUpLocations()

def main():
	inputFileName = getFileName()
	myMeasurements = Measurements()
	myMeasurements.readMeasurementsFile(inputFileName)
	myLocations = Locations()
	myFinder = Finder(myMeasurements.measurements, myLocations)
	myFinder.findLocations()
	return myFinder.locations.locations

def getFileName():
	try:
	    script, fileName = argv
	    return fileName
	except Exception, e:
		raise Exception("Please provide a file name.")

if __name__ == '__main__':
	try:
	    locations = main()
	    for location in locations:
		    print(location)
	except Exception, e:
		print(e)
