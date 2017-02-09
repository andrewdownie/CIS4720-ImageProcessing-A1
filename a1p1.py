#####
#####               Standard imports
#####
import sys


#####
#####               Relative imports
#####
thisDir = sys.path[0]
sys.path.append(thisDir + '/prof')
#from a1p1_code import *
import a1p1_code
from blurMetric import *
from imageIO import *
import imageIO
from morph import *
import morph

"""
import imenh_lib
import imfilter_lib
#import img_qi      #Is this a matplotlib file or something
import imhist_lib
import imrestore
import imthr_lib
import IPmetrics
import newALGS
"""

#####
#####               Program Setup
#####
args_list = ['inputFolder', 'outputFolder', 'inputImage', 'outputImage', 'algorithm', 'algorithmParameters']

args_dict = a1p1_code.ReadArgsFile(thisDir + '/args', args_list)
a1p1_code.PrintArgsDict(args_dict, True)

inputImage = args_dict['inputFolder'] + args_dict['inputImage']
outputImage = args_dict['outputFolder'] + args_dict['outputImage']


#####
#####               Read the image
#####
imageCr, imageCg, imageCb = imageIO.imread_colour(inputImage)


#####
#####               Process the image
#####
"""
print("\tMeasuring focus:")
focusMeasureCr = blurMetric.GRADfocus(imageCr)
focusMeasureCg = blurMetric.GRADfocus(imageCg)
focusMeasureCb = blurMetric.GRADfocus(imageCb)
print("Focus measure is: [" + str(focusMeasureCr) + ", " + str(focusMeasureCg) + ", " + str(focusMeasureCb) + "]")
"""

"""
print("Sharpening image:")
print("\tStarting one...")
newImgCr = morph.morph_sharp(imageCr)
print("\tStarting two...")
newImgCg = morph.morph_sharp(imageCg)
print("\tStarting three...")
newImgCb = morph.morph_sharp(imageCb)
"""



#####
#####               Output the image
#####
print("saving image...")
imageIO.imwrite_colour(outputImage, newImgCr, newImgCg, newImgCb)
