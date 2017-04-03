#!/bin/bash
#####
#####               Image-name, location and extensions
#####
imgName="compare"
relPath="images/" #relative to the script being run
inExt=".jpg"
outExt=".jpg"

#####
#####               The available algorithms to run
#####
morph_toggleCE="morph_toggleCE"
histhyper="histhyper"
morph_CE="morph_CE"
drew_CE="drew_CE"

seperator=" - "

IN_FILE="$relPath$imgName$inExt" 

#####
#####               FUNCTION: RunAlgo, takes the algorithm you want to run as parameter one 
#####
RunAlgo(){
    COMPARE_FILE="$relPath$imgName$seperator$1$outExt" 
    python ssim.py "$IN_FILE" "$COMPARE_FILE" 
}

#####
#####               Run the algorithms
#####
printf "morph toggle: "
RunAlgo "$morph_toggleCE"

printf "morph: "
RunAlgo "$morph_CE"

printf "histhyper: "
RunAlgo "$histhyper"

printf "drew: " 
RunAlgo "$drew_CE"

printf "\nrun.bash has finished\n\n"
