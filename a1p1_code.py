#####
#####               Imports
#####
import numpy
import math
import sys

from morph import *
import morph 


#####
#####               RGB to image
#####
def RGB_To_Image(img_r, img_g, img_b):
    rgbArray = numpy.zeros((img_r.shape[0],img_r.shape[1],3), 'uint8')
    rgbArray[..., 0] = img_r
    rgbArray[..., 1] = img_g
    rgbArray[..., 2] = img_b
    return rgbArray


#####
#####               Image to RGB
#####
def Image_To_RGB(img):
    resultRGB = numpy.asarray(img)
    img_r = resultRGB[:,:,0]
    img_g = resultRGB[:,:,1]
    img_b = resultRGB[:,:,2]
    return img_r, img_g, img_b

#####
#####               Image_rgb2yuv
#####
def Image_rgb2yuv(img_r, img_g, img_b):
# Calls rgb2yuv for every pixel in a color image 
    print('Image_rgb2yuv: row: ' + str(len(img_r)) + ' cols: ' + str(len(img_r[0])))
    img_y = numpy.zeros((img_r.shape[0], img_r.shape[1]))
    img_u = numpy.zeros((img_r.shape[0], img_r.shape[1]))
    img_v = numpy.zeros((img_r.shape[0], img_r.shape[1]))

    colCount = int(img_r.shape[0])
    rowCount = int(img_r.shape[1])

    for col in range(colCount):
        for row in range(rowCount):
            y, u, v = rgb2yuv(img_r[col, row], img_g[col, row], img_b[col, row]) 
            img_y[col, row] = math.floor(y)
            img_u[col, row] = math.floor(u)
            img_v[col, row] = math.floor(v)
             

    return img_y, img_u, img_v


#####
#####               Image_yuv2rgb
#####
def Image_yuv2rgb(img_y, img_u, img_v):
# Calls yuv2rgb for every pixel in a color image 
    print('Image_yuv2rgb: row: ' + str(len(img_y)) + ' cols: ' + str(len(img_y[0])))
    img_r = numpy.zeros((img_y.shape[0], img_y.shape[1]))
    img_g = numpy.zeros((img_y.shape[0], img_y.shape[1]))
    img_b = numpy.zeros((img_y.shape[0], img_y.shape[1]))

    colCount = int(img_y.shape[0])
    rowCount = int(img_y.shape[1])

    for col in range(colCount):
        for row in range(rowCount):
            r, g, b = yuv2rgb(img_y[col, row], img_u[col, row], img_v[col, row]) 
            img_r[col, row] = r
            img_g[col, row] = g
            img_b[col, row] = b
             

    return img_r, img_g, img_b

#####
#####               rgb2yuv
#####
def rgb2yuv(r, g, b):
# Ported from a js version, see rgb2yuv.js file for more details
    y = r * 0.299000 + g * 0.587000 + b * 0.114000
    u = r * -0.168736 + g * -0.331264 + b * 0.5000000 + 128
    v = r * 0.500000 + g * - 0.418688 + b * -0.081312 + 128    

    return y, u, v


#####
#####               yuv2rgb
#####
def yuv2rgb(y, u, v):
   r = y + 1.4075 * (v - 128)
   g = y - 0.3455 * (u - 128) - (0.7169 * (v - 128))
   b = y + 1.7790 * (u - 128) 


   if(r < 0):
       r = 0
   elif(r > 255):
       r = 255

   if(g < 0):
       g = 0
   elif(g > 255):
       g = 255

   if(b < 0):
       b = 0
   elif(b > 255):
       b = 255


 

   return r, g, b

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
def morph_CE(img_r, img_g, img_b):
    print('-- Starting morph_CE')

    newCr = morph.morph_CE(img_r)
    print('- Done red')
    newCg = morph.morph_CE(img_g)
    print('- Done green')
    newCb = morph.morph_CE(img_b)
    print('- Done blue')

    print('-- Ending morph_CE')
    

    return newCr, newCg, newCb


#####
#####               morph_toggleCE 
#####
def morph_toggleCE(img_r, img_g, img_b, nBlocks=20):
    print('-- Starting morph_toggleCE')

    newCr = morph.morph_toggleCE(img_r)
    print('- Done red')
    newCg = morph.morph_toggleCE(img_g)
    print('- Done green')
    newCb = morph.morph_toggleCE(img_b)
    print('- Done blue')

    print('-- Ending morph_toggleCE')

    return newCr, newCg, newCb


#####
#####               DREW
#####
def DREW(img_r, img_g, img_b):
    print('-- Starting DREW')
    imgRGB = RGB_To_Image(img_r, img_g, img_b)
    
    print('r is: ' + str(img_r.mean()))
    print('g is: ' + str(img_g.mean()))
    print('b is: ' + str(img_b.mean()))


    #idea: bring all 3 channels to an average of 127 mean value
    #HOW?
    #figure out the ratio between desired (127) and actual
    #so if actual for red was 53, the ratio would be 127/53 = 2.396, which is what you multiply actual to get 127
    #you also want to take into account the actual value of each pixel, the further each pixel the larger the adjustment? or does that work?
    
    redCo = 127.5 / img_r.mean()
    print('redCo is: ' + str(redCo))


    newimg_r = [pixel * redCo for pixel in img_r]

    print('-- Ending DREW')

    return newimg_r, img_g, img_b


