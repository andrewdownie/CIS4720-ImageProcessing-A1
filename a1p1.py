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

#####
#####               Program Setup
#####
inputImage, outputImage, algo = ReadCLArgs()

print('')
print('inputImage is:\t' + inputImage)
print('outputImage is:\t' + outputImage)
print('algo is:\t' + algo)
print('')

#####
#####               Read the image
#####
imgCr, imgCg, imgCb = imageIO.imread_colour(inputImage)
#bw_image = imageIO.imread_gray(inputImage)


#####
#####               Process the image
#####
if algo == 'grayWorld':
    a1p1_code.grayWorld(imgCr, imgCg, imgCb)

elif algo == 'maxWhite':
    a1p1_code.maxWhite(imgCr, imgCg, imgCb)

elif algo == 'SDWGW':
    a1p1_code.SDWGW(imgCr, imgCg, imgCb, 20)


#####
#####               Output the image
#####
print("saving image...")
imageIO.imwrite_colour(outputImage, imgCr, imgCg, imgCb)
