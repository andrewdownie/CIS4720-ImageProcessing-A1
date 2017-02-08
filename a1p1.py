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
import blurMetric
from imageIO import *       #Need to do this for all imports
import imenh_lib
import imfilter_lib
#import img_qi      #Is this a matplotlib file or something
import imhist_lib
import imrestore
import imthr_lib
import IPmetrics
import morph
import newALGS


#####
#####               Arguments list
#####
args_list = ['inputFolder', 'outputFolder', 'inputImage', 'outputImage', 'algorithm', 'algorithmParameters']



#####
#####               Run the program
#####
args_dict = ReadArgsFile(thisDir + '/args', args_list)
PrintArgsDict(args_dict, True)

inputImage = args_dict['inputFolder'] + args_dict['inputImage']
outputImage = args_dict['outputFolder'] + args_dict['outputImage']

imageCr, imageCg, imageCb = imageIO.imread_colour(inputImage)
imageIO.imwrite_colour(outputImage, imageCr, imageCg, imageCb)
