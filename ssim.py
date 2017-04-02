import sys



thisDir = sys.path[0]
sys.path.append(thisDir + '/lib')


from imageIO import *
import imageIO


if(len(sys.argv) != 3):
    print("you must provide exactly two paths to images, as parameters to this program,\nexiting...")
    sys.exit()


imageOne = thisDir + "/" + sys.argv[1]
imageTwo = thisDir + "/" + sys.argv[2]

