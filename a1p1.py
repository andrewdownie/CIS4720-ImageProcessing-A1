#####
#####               Standard imports
#####
import sys

#####
#####               Relative imports
#####
thisDir = sys.path[0]
sys.path.append(thisDir + '/lib')

from a1p1_code import *
import a1p1_code

from imageIO import *
import imageIO

#####
#####               Get command line args 
#####
inputImage, outputImage, algo = ReadCLArgs(thisDir)

print('\nCommand line arguments:')
print('\tinputImage is: ' + inputImage)
print('\toutputImage is: ' + outputImage)
print('\talgo is: ' + algo)
print('')

#####
#####               Read the image
#####
img_r, img_g, img_b = imageIO.imread_colour(inputImage)


y, u, v = rgb2yuv(255, 0, 4)

print("y is: " + str(y))
print("u is: " + str(u))
print("v is: " + str(v))

r, g, b = yuv2rgb(y, u, v)

  
print("r is: " + str(r))
print("g is: " + str(g))
print("b is: " + str(b))

#####
#####               Process the image
#####
if algo == 'morph_toggleCE':
    new_r, new_g, new_b = a1p1_code.morph_toggleCE(img_r, img_g, img_b)

elif algo == 'morph_CE':
    new_r, new_g, new_b = a1p1_code.morph_CE(img_r, img_g, img_b)

elif algo == 'DREW':
    new_r, new_g, new_b = a1p1_code.DREW(img_r, img_g, img_b)

else:
    print('No algo was selected, exiting program...')
    sys.exit()


#####
#####               Output the image
#####

print("\nsaving image...\n")
imageIO.imwrite_colour(outputImage, new_r, new_g, new_b)
                        