#!/usr/bin/env python
import os

AVOEXTPATH=os.path.join(os.environ["HOME"],".avogadro/extensionScripts")

LIBFILES = ["pyquante/surfaces.py"]
EXTS = ["surface_ext.py"]
def devel():
    for file in LIBFILES:
        # src dest        
        dest = os.path.join(AVOEXTPATH,"lib",os.path.basename(file))
        os.link(file,
                dest)
    for file in EXTS:
        os.link(file, AVOEXTPATH)

commands = {
    "devel" : devel
}
if __name__ == '__main__':
    import sys
    cmd = sys.argv[1]
    commands[cmd]()
    
