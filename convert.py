#!/usr/bin/env python3

import os, sys, time
import xml.etree.ElementTree as ET
from utils import load_config, pretty_print_json, createDirectory

CONFIG_FILE = "config.yml"

class dataConverter(object):
  """Conver Polar Excercise XML data files to CSV and GeoJSON formats"""

  def __init__(self):
    self.config = load_config(CONFIG_FILE)

    self.config['gpx']  = self.config['dataDir'] + '/gpx'
    self.config['json'] = self.config['dataDir'] + '/json'

    createDirectory(self, self.config['gpx'])
    createDirectory(self, self.config['json'])


  def cleanOldDataFiles(self):
    """Find and remove old gpx data files"""


  def listFiles(self):
    print('List available .gpx files:')
    """List gps datafiles in data directory"""
    gpxFiles = []

    for f in os.listdir(self.config['gpx']):
      print(f)
      gpxFiles.append(f)

    return gpxFiles


  def writeToFile(self, fileName, format, data):
    print('Write data to file:')
    file = str(self.config['dataDir'])+'/'+str(format)+'/'+str(fileName)+'.'+str(format)
    print('file:',file)
    f = open(file,'w+')
    f.write(data)
    f.close()


  def parseAndConvert(self):
    """Parse and convert gpx data files to geojson"""
    files = self.listFiles()
    coordinates = []
    print('......................................')
    for f in files:
      print('Parse and convert datafile:',f)
      file = self.config['gpx']+'/'+f
      fileName = file.split('.')[0]
      fileName = fileName.split('/')[-1]
      root = ET.parse(self.config['gpx']+'/'+f).getroot()
      for child in root:
        for child in child:
          if 'trkseg' in child.tag: 
            for child in child:
              coordinates.append([child.attrib['lon'],child.attrib['lat']])

      geos = []
      feature = {
        'type': 'Feature',
        'type': 'LineString',
        'geometry': {
          'type': 'LineString',
          'coordinates': [[lon,lat] for lon,lat in coordinates]
        },
        'properties': {
            'prop0': 'value0'
        }
      }
      geos.append(feature)
      geometries = {
        'type': 'FeatureCollection',
        'features': geos,
      }
      self.writeToFile(fileName, 'json', pretty_print_json(geometries))
      print('......................................')



if __name__ == "__main__":
    converter = dataConverter()
    converter.parseAndConvert()