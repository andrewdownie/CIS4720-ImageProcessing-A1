#!/bin/bash
rootPath="/mnt/c/Users/drew/OneDrive/School/CIS 4720 - Image Processing/images/"
inPath="part1/"
outPath=""

imgName="white_balance"
inExt=".jpg"
outExt=".jpg"

grayWorld="grayWorld"
maxWhite="maxWhite"
SDWGW="SDWGE"
UNDERSCORE="_"

INPUT_FILE="$rootPath$inPath$imgName$inExt" 
OUTPUT_FILE="$rootPath$outPath$imgName$UNDERSCORE" 

ALGO="$SDWGW"
python a1p1.py "$INPUT_FILE" "$OUTPUT_FILE$ALGO$outExt" "$ALGO"\