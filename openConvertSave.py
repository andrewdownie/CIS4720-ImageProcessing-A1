
import os
import PIL
from PIL import Image

infile = "images/inputImg.png"
outfile = "images/outputImg.jpg"


if infile != outfile:
    try:
        Image.open(infile).save(outfile)
    except IOError:
        print("cannot convert " + infile)
