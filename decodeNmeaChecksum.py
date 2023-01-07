import operator
from functools import reduce

# Decode checksum
def decodeNmeaChecksum(string: str):
	# This function checks the validity of an NMEA string using it's checksum
	# Remove unused characters
	string = string.strip("$\n")
	# Split data and hex
	nmeaData, checksum = string.split("*", 1)
	# Verify that the sum of all the characters match the hex value received
	calculatedChecksum = reduce(operator.xor, (ord(s) for s in nmeaData), 0)
	if int(checksum, base=16) == calculatedChecksum:
		return nmeaData
	else:
		raise ValueError("The NMEA data does not match it's checksum")