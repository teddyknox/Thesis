#!/usr/bin/env python
# sic: Sort Image Colors
import sys, os, inspect
APP_DIRNAME = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))))
sys.path.append(APP_DIRNAME)

from PIL import Image

def main():
    assert len(sys.argv) >= 2
    filename = os.path.abspath(argv[1])
    image = Image.open(filename)


if __name__ == "__main__":
    main()
