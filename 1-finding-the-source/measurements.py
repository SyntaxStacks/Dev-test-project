from reading import Reading

class Measurements():
	def __init__(self):	
		self.measurements = []

	def readMeasurementsFile(self, fileName):
		try:
			with open(fileName, 'r') as inputFile:
				for line in inputFile:
					x, y, distance = line.split()
					self.addMeasurement(Reading(x, y, distance))
		except Exception, e:
			self.measurements = []
			raise Exception("Unable to read measurements from file.")

	def addMeasurement(self, reading):
		if reading not in self.measurements:
			self.measurements.append(reading)

	def printMeasurements(self):
		for reading in self.measurements:
			print(reading)