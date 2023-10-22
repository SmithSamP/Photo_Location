import os
import simplekml
from GPSPhoto import gpsphoto
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    return exif_table


def create_KML(dirPath, savePath, count, icon, size, kml):
    # Get all the files in the current directory.
    files = os.listdir(dirPath)
    # Iterate over all the files.
    for file in files:
        # Check if the file is an image file.
        filePath = dirPath + '\\' + file
        if os.path.isfile(filePath) and file.endswith('.jpg') or file.endswith('.png'):

            try:
                data = gpsphoto.getGPSData(filePath)
                long = data["Longitude"]
                lat = data["Latitude"]
            except:
                try:
                    f = open("error_logging.txt", "a")

                    # writing in the file
                    f.write(str(filePath + ' No coordinates\n'))

                    # closing the file
                    f.close()
                except PermissionError:
                    continue
                continue

            # Apply the function to the file.
            pnt = kml.newpoint(name=file)
            pnt.coords = [(long, lat)]
            pnt.description = fr'<img style="max-width:{size}px;" src="file:///{filePath}">'
            style = simplekml.Style()
            if icon:
                pnt.style.iconstyle.icon.href = filePath
            else:
                pnt.style.iconstyle.icon.href = r'http://maps.google.com/mapfiles/kml/shapes/square.png'
            pnt.style.iconstyle.scale = 0.66
            pnt.style.labelstyle.scale = 0
        # Check if the file is a directory.
        elif os.path.isdir(filePath):
            count += 1
            # Recursively call the function on the directory.
            create_KML(filePath, savePath, count, icon, size, kml)


def run_KML(dirPath, savePath, count, icon, size):
    kml = simplekml.Kml()
    f = open("error_logging.txt", "a")
    f.write('')
    f.close()
    create_KML(dirPath, savePath, count, icon, size, kml)
    kml.save(savePath)
