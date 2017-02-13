#####
#####               Imports
#####
import sys
"""
import blurMetric
import imageIO
import imenh_lib
import imfilter_lib
#import img_qi      #Is this a matplotlib file or something
import imhist_lib
import imrestore
import imthr_lib
import IPmetrics
import morph
import newALGS
"""

#####
#####               Read command line args
#####
def ReadCLArgs():
    inputImage = sys.argv[1]
    outputImage = sys.argv[2]
    algoList = sys.argv[3]
    return inputImage, outputImage, algoList