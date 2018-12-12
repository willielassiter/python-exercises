import os

def traverse (path):

    for basepath, directories, files in os.walk (path):
        for f in files:
            print (os.path.join (basepath, f))


# traverse (os.path.expanduser ("~"))

import pathlib

print (pathlib.Path ('traverse.py').stat().st_mode)