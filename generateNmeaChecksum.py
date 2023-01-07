import operator
from functools import reduce

# Generate the checksum format
def generateNmeaChecksum(sentence: str):
	calculatedChecksum = reduce(operator.xor, (ord(s) for s in sentence), 0)
	calculatedChecksum = f'{calculatedChecksum:X}'
	sentence = f'${sentence}*{calculatedChecksum}'
	return sentence