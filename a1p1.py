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
inputImage, outputImage, algo = ReadCLArgs()

print('\nCommand line arguments:')
print('\tinputImage is:\t' + inputImage)
print('\toutputImage is:\t' + outputImage)
print('\talgo is:\t' + algo)
print('')

#####
#####               Read the image
#####
imgCr, imgCg, imgCb = imageIO.imread_colour(inputImage)


#####
#####               Process the image
#####
if algo == 'grayWorld':
    resultImgRGB = a1p1_code.grayWorld(imgCr, imgCg, imgCb)

elif algo == 'maxWhite':
    resultImgRGB = a1p1_code.maxWhite(imgCr, imgCg, imgCb)

elif algo == 'SDWGW':
    resultImgRGB = a1p1_code.SDWGW(imgCr, imgCg, imgCb, 20)


#####
#####               Output the image
#####
print('\nunpacking image...')
resultImgCr = resultImgRGB[:,:,0]
resultImgCg = resultImgRGB[:,:,1]
resultImgCb = resultImgRGB[:,:,2]

print("\nsaving image...\n")
imageIO.imwrite_colour(outputImage, resultImgCr, resultImgCg, resultImgCb)
                        