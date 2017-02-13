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
from blurMetric import *

from imageIO import *
import imageIO

from morph import *
import morph

from newALGS import *
import newALGS



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
inputImage, outputImage, algoList = ReadCLArgs()
print('Input image is: ' + inputImage)

#####
#####               Read the image
#####
imageCr, imageCg, imageCb = imageIO.imread_colour(inputImage)
#bw_image = imageIO.imread_gray(inputImage)


#####
#####               Process the image
#####
"""
print("\tMeasuring focus:")
print("\tStarting red...")
focusMeasureCr = blurMetric.GRADfocus(imageCr)
print("\tStarting green...")
focusMeasureCg = blurMetric.GRADfocus(imageCg)
print("\tStarting b...")
focusMeasureCb = blurMetric.GRADfocus(imageCb)
print("Focus measure is: [" + str(focusMeasureCr) + ", " + str(focusMeasureCg) + ", " + str(focusMeasureCb) + "]")
"""

print("\tStarting one...")
newImgCr = newALGS.nagao_matsuyama(imageCr)
print("\tStarting two...")
newImgCg = newALGS.nagao_matsuyama(imageCg)
print("\tStarting three...")
newImgCb = newALGS.nagao_matsuyama(imageCb)






#print("shapening black white image")
#new_bw_image = morph.morph_sharp(bw_image)



#####
#####               Output the image
#####
print("saving image...")
imageIO.imwrite_colour(outputImage, newImgCr, newImgCg, newImgCb)
#imageIO.imwrite_gray(outputImage, new_bw_image)
