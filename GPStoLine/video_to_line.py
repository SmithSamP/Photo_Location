import telemetry_parser
import logging
import simplekml

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

in_video = r"\\aks-dronenas\360Video\11756\20241025\11756 20241025 360video 03.360"

tp = telemetry_parser.Parser(in_video)


coordinates = []
coordinate_tuples = []
telemetry = tp.telemetry()
logging.info(F'Telemetry has {len(telemetry)} chunks', )

for chunk in telemetry:
    if 'GPS' in chunk:
        coordinate_list = chunk['GPS']['Data']
        coordinates.extend(coordinate_list)
    
for coordinate in coordinates:
    new_tuple = (coordinate[1]/10000000, coordinate[0]/10000000, coordinate[2]/10000)
    coordinate_tuples.append(new_tuple)

logging.info(f'Found {len(coordinates)} coordinates', )





kml = simplekml.Kml()
ls = kml.newlinestring(name='A LineString')
ls.coords = coordinate_tuples
ls.extrude = 1
ls.altitudemode = simplekml.AltitudeMode.clamptoground
kml.save("LineString.kml")

