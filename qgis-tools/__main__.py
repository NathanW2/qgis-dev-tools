"""
QGIS dev tools
"""

#!/usr/bin/env python3

import os
import argparse
import qgis_tools

ROOTFOLDER = os.getcwd()

print("Running environment")
print("Root Folder:{0}".format(ROOTFOLDER))

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('--code-format', action='store_true',
                    help='Format code to QGIS style.')

parser.add_argument('--prepare-commit', action='store_true',
                    help='Run precommit formatting')

parser.add_argument('--root-folder', type=str,
                    help='Path to the root folder of QGIS src',
                    default=ROOTFOLDER)
                   
args = parser.parse_args()

qgis_tools.main(args)