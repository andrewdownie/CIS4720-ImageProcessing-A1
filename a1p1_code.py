#####
#####               Imports
#####
import sys

import numpy

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



#####
#####               grayWorld      
#####
def grayWorld(imgCr, imgCg, imgCb):

    print('<<Starting grayWorld')
    imageRGB = numpy.array([imgCr, imgCg, imgCb])
    result = imrestore.grayWorld(imageRGB)
    resultRGB = numpy.asarray(result)
    imgCr = resultRGB[:, :, 0]
    imgCg = resultRGB[:, :, 1]
    imgCb = resultRGB[:, :, 2]
    print('Ending grayWorld>>')

    return imgCr, imgCg, imgCb 

#####
#####               maxWhite
#####
def maxWhite(imgCr, imgCg, imgCb):
    print('<<Starting maxWhite')
    rgbArray = RGB_To_Image(imgCr, imgCg, imgCb)
    print(rgbArray.shape)

    result = imrestore.maxWhite(rgbArray)
    imgCr, imgCg, imgCb = Image_To_RGB(result)
    print('Ending maxWhite>>')
    

    return imgCr, imgCg, imgCb


#####
#####               SDWGW
#####
def SDWGW(imgCr, imgCg, imgCb, nBlocks=20):
    print('this is SDWGW')