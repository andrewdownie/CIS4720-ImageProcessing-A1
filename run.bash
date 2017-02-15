#!/bin/bash
#####
#####               Input path
#####
path="images/"

#####
#####               Image-name and image file extensions
#####
imgName="white_balance"
inExt=".jpg"
outExt=".jpg"

#####
#####               The available algorithms to run
#####
grayWorld="grayWorld"
maxWhite="maxWhite"
SDWGW="SDWGE"

#So I don't need to learn how bash concatenation 'actually' works
underscore="_"

IN_FILE="$path$imgName$inExt" 


ALGO="$SDWGW"
OUT_FILE="$path$imgName$underscore$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\

ALGO="$grayWorld"
OUT_FILE="$path$imgName$underscore$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\

ALGO="$maxWhite"
OUT_FILE="$path$imgName$underscore$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\