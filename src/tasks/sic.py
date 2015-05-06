#!/usr/bin/env python
# sic: Sort Image Colors

import sys, os
from PIL import Image

def main():
    assert len(sys.argv) >= 2
    filename = os.path.abspath(argv[1])
    image = Image.open(filename)


if __name__ == "__main__":
    main()
