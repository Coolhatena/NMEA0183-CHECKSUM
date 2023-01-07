from generateNmeaChecksum import generateNmeaChecksum
from decodeNmeaChecksum import decodeNmeaChecksum

nmeaChecksum = generateNmeaChecksum(input('Write the checksum target string: '))
print(f'This is the generated NMEA checksum: {repr(nmeaChecksum)}')
print(f'Decoded NMEA checksum: {repr(decodeNmeaChecksum(nmeaChecksum))}')
