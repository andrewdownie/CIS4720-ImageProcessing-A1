#####
#####               Imports
#####
import sys


from imrestore import *
import imrestore
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
    inputImage = ''
    outputImage = ''
    algo = ''

    for i in range(1, 4):
        keyVal = sys.argv[i].split('=')
        if(keyVal[0] == 'inputImage'):
            inputImage = keyVal[1]
        elif(keyVal[0] == 'outputImage'):
            outputImage = keyVal[1]
        elif(keyVal[0] == 'algo'):
            algo = keyVal[1]

    return inputImage, outputImage, algo



# img_filter         - Image filtering with a 3x3 kernel
# img_filterMEAN     - Image smoothing with a 3x3 neighbourhood
# img_filterGAUSSIAN - Image smoothing with Gaussian filter
# img_sharpUSM       - Image sharpening with unsharp masking
# img_sharpUSMgauss  - Image sharpening using Gaussian
# img_sharpCUSM      - Image sharpening with Cubic UM

#####
#####               grayWorld      
#####
def grayWorld(imgCr, imgCg, imgCb):
    print('this is grayworld')



#####
#####               maxWhite
#####
def maxWhite(imgCr, imgCg, imgCb):
    print('this is maxWhite')


#####
#####               SDWGW
#####
def SDWGW(imgCr, imgCg, imgCb, nBlocks=20):
    print('this is SDWGW')