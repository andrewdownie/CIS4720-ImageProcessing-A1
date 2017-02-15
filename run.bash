#!/bin/bash
#rootPath="/mnt/c/Users/drew/OneDrive/School/CIS 4720 - Image Processing/images/"
rootPath="images/"
inPath="part1/"
outPath=""

imgName="white_balance"
inExt=".jpg"
outExt=".jpg"

grayWorld="grayWorld"
maxWhite="maxWhite"
SDWGW="SDWGE"
underscore="_"

IN_FILE="$rootPath$inPath$imgName$inExt" 


ALGO="$SDWGW"
OUT_FILE="$rootPath$outPath$imgName$underscore$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\

#ALGO="$grayWorld"
#OUT_FILE="$rootPath$outPath$imgName$underscore$ALGO$outExt" 
#python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\

#ALGO="$maxWhite"
#OUT_FILE="$rootPath$outPath$imgName$underscore$ALGO$outExt" 
#python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\