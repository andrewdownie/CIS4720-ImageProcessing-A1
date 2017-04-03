import sys
import PIL



thisDir = sys.path[0]
sys.path.append(thisDir + '/lib')


from a1p1_code import *
import a1p1_code

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

img1_y, img1_u, img1_v = Image_rgb2yuv(img1_r, img1_g, img1_b)
img2_y, img2_u, img2_v = Image_rgb2yuv(img2_r, img2_g, img2_b)

index = IPmetrics.SSIM(img1_y, img2_y)

print("SSIM index is: " + str(index))

