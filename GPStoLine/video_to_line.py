import telemetry_parser
import logging
import simplekml
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class VideoToLine:

    def __init__(self, input_video, save_path):
        self.input_video = input_video
        self.save_path = save_path
        self.coordinate_tuples = None

    def get_coordinates(self):
        

        tp = telemetry_parser.Parser(self.input_video)
        coordinates = []
        coordinate_tuples = []
        telemetry = tp.telemetry()

        for chunk in telemetry:
            if 'GPS' in chunk:
                coordinate_list = chunk['GPS']['Data']
                coordinates.extend(coordinate_list)
            
        for coordinate in coordinates:
            new_tuple = (coordinate[1]/10000000, coordinate[0]/10000000, coordinate[2]/10000)
            coordinate_tuples.append(new_tuple)

        logging.info(f'Found {len(coordinates)} coordinates', )
        self.coordinate_tuples = coordinate_tuples

    def create_kml(self):
        if self.coordinate_tuples is None:
            logging.error('No coordinates found')
            return

        file_name = os.path.basename(self.save_path)
        kml = simplekml.Kml()
        ls = kml.newlinestring(name=file_name)
        ls.coords = coordinate_tuples
        ls.extrude = 1
        ls.altitudemode = simplekml.AltitudeMode.clamptoground
        ls.style.linestyle.width = 3
        ls.style.linestyle.color = simplekml.Color.red
        kml.save(self.save_path)
        

