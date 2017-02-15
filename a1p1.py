#####
#####               Standard imports
#####
import sys

#####
#####               Relative imports
#####
thisDir = sys.path[0]
sys.path.append(thisDir + '/prof')

from a1p1_code import *
import a1p1_code

from imageIO import *
import imageIO

#####
#####               Get command line args 
#####
inputImage, outputImage, algo = ReadCLArgs(thisDir)

print('\nCommand line arguments:')
print('\tinputImage is: ' + inputImage)
print('\toutputImage is: ' + outputImage)
print('\talgo is: ' + algo)
print('')

#####
#####               Read the image
#####
imgCr, imgCg, imgCb = imageIO.imread_colour(inputImage)


#####
#####               Process the image
#####
if algo == 'grayWorld':
    imgCr, imgCg, imgCb = a1p1_code.grayWorld(imgCr, imgCg, imgCb)

elif algo == 'maxWhite':
    imgCr, imgCg, imgCb = a1p1_code.maxWhite(imgCr, imgCg, imgCb)

elif algo == 'SDWGW':
    a1p1_code.SDWGW(imgCr, imgCg, imgCb, 20)


#####
#####               Output the image
#####

print("\nsaving image...\n")
imageIO.imwrite_colour(outputImage, imgCr, imgCg, imgCb)
                        