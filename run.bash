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

#####
#####               FUNCTION: RunAlgo, takes the algorithm you want to run as parameter one 
#####
RunAlgo(){
    OUT_FILE="$relPath$imgName$seperator$1$outExt" 
    python a1p1.py "$IN_FILE" "$OUT_FILE" "$1"
}

#####
#####               Run the algorithms
#####
RunAlgo "$morph_CE"
exit

RunAlgo "$morph_toggleCE"

RunAlgo "$DREW"