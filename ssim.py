import sys
import PIL



thisDir = sys.path[0]
sys.path.append(thisDir + '/lib')


from a1p1_code.py import *
import a1p1_cody.py

from imageIO import *
import imageIO

from IPmetrics import *
import IPmetrics



if(len(sys.argv) != 3):
    print("you must provide exactly two paths to images, as parameters to this program,\nexiting...")
    sys.exit()


imagePathOne = thisDir + "/" + sys.argv[1]
imagePathTwo = thisDir + "/" + sys.argv[2]

img1_r, img1_g, img1_b = imageIO.imread_colour(imagePathOne)
img2_r, img2_g, img2_b = imageIO.imread_colour(imagePathTwo)

#convert the rgb to huv, and then combine them into one image
#IPmetrics.ssim()

