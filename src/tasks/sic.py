#!/usr/bin/env python
# sic: Sort Image Colors
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__name__)))

from PIL import Image

def main():
    assert len(sys.argv) >= 2
    filename = os.path.abspath(argv[1])
    image = Image.open(filename)


if __name__ == "__main__":
    main()
