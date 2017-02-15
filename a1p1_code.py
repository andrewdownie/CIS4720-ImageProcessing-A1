#####
#####               Imports
#####
import numpy
import sys

from imrestore import *
import imrestore


#####
#####               RGB to image
#####
def RGB_To_Image(imgCr, imgCg, imgCb):
    rgbArray = numpy.zeros((imgCr.shape[0],imgCr.shape[1],3), 'uint8')
    rgbArray[..., 0] = imgCr
    rgbArray[..., 1] = imgCg
    rgbArray[..., 2] = imgCb
    return rgbArray


#####
#####               Image to RGB
#####
def Image_To_RGB(img):
    resultRGB = numpy.asarray(img)
    imgCr = resultRGB[:,:,0]
    imgCg = resultRGB[:,:,1]
    imgCb = resultRGB[:,:,2]
    return imgCr, imgCg, imgCb


#####
#####               Read command line args
#####
def ReadCLArgs(thisDir):
    if(len(sys.argv) < 4):
        print('not enough command line args, errors happen now:')

    inputImage = thisDir + "/" + sys.argv[1] 
    outputImage = thisDir + "/" + sys.argv[2] 
    algo = sys.argv[3] 

    return inputImage, outputImage, algo



#####
#####               grayWorld      
#####
def grayWorld(imgCr, imgCg, imgCb):

    print('-- Starting grayWorld')

    rgbArray = RGB_To_Image(imgCr, imgCg, imgCb)
    result = imrestore.grayWorld(rgbArray)
    imgCr, imgCg, imgCb = Image_To_RGB(result)

    print('-- Ending grayWorld')

    return imgCr, imgCg, imgCb 

#####
#####               maxWhite
#####
def maxWhite(imgCr, imgCg, imgCb):
    print('-- Starting maxWhite')

    rgbArray = RGB_To_Image(imgCr, imgCg, imgCb)
    result = imrestore.maxWhite(rgbArray)
    imgCr, imgCg, imgCb = Image_To_RGB(result)

    print('-- Ending maxWhite')
    

    return imgCr, imgCg, imgCb


#####
#####               SDWGW
#####
def SDWGW(imgCr, imgCg, imgCb, nBlocks=20):
    print('-- Starting SDWGW')

    rgbArray = RGB_To_Image(imgCr, imgCg, imgCb)
    result = imrestore.SDWGW(rgbArray)
    imgCr, imgCg, imgCb = Image_To_RGB(result)

    print('-- Ending SDWGW')