#!/bin/bash
#####
#####               Image-name, location and extensions
#####
imgName="lowcontrast"
relPath="images/" #relative to the script being run
inExt=".jpg"
outExt=".jpg"

#####
#####               The available algorithms to run
#####
morph_toggleCE="morph_toggleCE"
morph_CE="morph_CE"
DREW="DREW"

seperator=" - "

IN_FILE="$relPath$imgName$inExt" 

ALGO="$morph_CE"
OUT_FILE="$relPath$imgName$seperator$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\

exit

ALGO="$morph_toggleCE"
OUT_FILE="$relPath$imgName$seperator$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\


exit #dont run my algo, it doesnt work yet

ALGO="$DREW"
OUT_FILE="$relPath$imgName$seperator$ALGO$outExt" 
python a1p1.py "$IN_FILE" "$OUT_FILE" "$ALGO"\