#####
#####               Imports
#####
import numpy
import sys

from morph import *
import morph 


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
#####               morph_CE 
#####
def morph_CE(imgCr, imgCg, imgCb):
    print('-- Starting morph_CE')

    newCr = morph.morph_CE(imgCr)
    print('- Done red')
    newCg = morph.morph_CE(imgCg)
    print('- Done green')
    newCb = morph.morph_CE(imgCb)
    print('- Done blue')

    print('-- Ending morph_CE')
    

    return newCr, newCg, newCb


#####
#####               morph_toggleCE 
#####
def morph_toggleCE(imgCr, imgCg, imgCb, nBlocks=20):
    print('-- Starting morph_toggleCE')

    newCr = morph.morph_toggleCE(imgCr)
    print('- Done red')
    newCg = morph.morph_toggleCE(imgCg)
    print('- Done green')
    newCb = morph.morph_toggleCE(imgCb)
    print('- Done blue')

    print('-- Ending morph_toggleCE')

    return newCr, newCg, newCb


#####
#####               DREW
#####
def DREW(imgCr, imgCg, imgCb):
    print('-- Starting DREW')
    imgRGB = RGB_To_Image(imgCr, imgCg, imgCb)
    
    print('r is: ' + str(imgCr.mean()))
    print('g is: ' + str(imgCg.mean()))
    print('b is: ' + str(imgCb.mean()))


    #idea: bring all 3 channels to an average of 127 mean value
    #HOW?
    #figure out the ratio between desired (127) and actual
    #so if actual for red was 53, the ratio would be 127/53 = 2.396, which is what you multiply actual to get 127
    #you also want to take into account the actual value of each pixel, the further each pixel the larger the adjustment? or does that work?
    
    redCo = 127.5 / imgCr.mean()
    print('redCo is: ' + str(redCo))


    newImgCr = [pixel * redCo for pixel in imgCr]

    print('-- Ending DREW')

    return newImgCr, imgCg, imgCb