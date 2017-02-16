#####
#####               Standard imports
#####
import sys

#####
#####               Relative imports
#####
thisDir = sys.path[0]
sys.path.append(thisDir + '/lib')

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
if algo == 'morph_toggleCE':
    newCr, newCg, newCb = a1p1_code.morph_toggleCE(imgCr, imgCg, imgCb)

elif algo == 'morph_CE':
    newCr, newCg, newCb = a1p1_code.morph_CE(imgCr, imgCg, imgCb)

elif algo == 'DREW':
    newCr, newCg, newCb = a1p1_code.DREW(imgCr, imgCg, imgCb)

else:
    print('No algo was selected, exiting program...')
    sys.exit()


#####
#####               Output the image
#####

print("\nsaving image...\n")
imageIO.imwrite_colour(outputImage, newCr, newCg, newCb)
                        