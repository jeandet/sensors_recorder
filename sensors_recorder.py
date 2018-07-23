#!/usr/bin/env python3

__author__ = "Alexis Jeandet"
__copyright__ = "Copyright 2017, Laboratory of Plasma Physics"
__credits__ = []
__license__ = "GPLv2"
__version__ = "1.0.0"
__maintainer__ = "Alexis Jeandet"
__email__ = "alexis.jeandet@member.fsf.org"
__status__ = "Development"

import importlib
import traceback
import os
import argparse
import configparser
from os.path import expanduser
home = expanduser("~")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--config-file", help="config file", default=home+'/.lpp_backup.conf')
parser.add_argument("--list-modules", help="lists available modules", action="store_true")
parser.add_argument("--sim", help="Simulation mode, just print commands", action="store_true")
args = parser.parse_args()


if __name__ == '__main__':

    config = configparser.ConfigParser()
    print(args.config_file)
    config.read(args.config_file)

    sensors_groups = dict(config)
    monitors = []
    for group, group_config in sensors_groups.items():
        monitors.append(importlib.import_module(group_config["module"]))
