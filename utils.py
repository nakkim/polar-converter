#!/usr/bin/env python3

import json, yaml, os


def load_config(filename):
  """Load configuration from a yaml file"""
  with open(filename) as f:
    return yaml.load(f)

def pretty_print_json(data):
  return json.dumps(data, indent=4, sort_keys=True)


def createDirectory(self, dirName):
  """Create data directories"""
  if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " + dirName +  " Created")
  # else:
    # print("Directory " + dirName +  " already exists")