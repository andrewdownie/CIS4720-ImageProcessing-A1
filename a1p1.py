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


#####
#####               Arguments list
#####
args_list = ['inputImage', 'outputImage', 'algorithm', 'algorithmParameters']


#####
#####               Run the program
#####
args_dict = ReadArgsFile(thisDir + '/args', args_list)
PrintArgsDict(args_dict, True)
