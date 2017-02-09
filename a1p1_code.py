#####
#####               Imports
#####
"""
import blurMetric
import imageIO
import imenh_lib
import imfilter_lib
#import img_qi      #Is this a matplotlib file or something
import imhist_lib
import imrestore
import imthr_lib
import IPmetrics
import morph
import newALGS
"""


#####
#####               Read args file
#####
def ReadArgsFile(filePath, args_list):
    args_dict = {}

    args_path = filePath
    args = open(args_path, 'r').read()

    args_lines = args.splitlines()


    for arg_line in args_lines:
        arg_kv = arg_line.split(':', 1)
        arg_key = arg_kv[0].strip()
        arg_val = arg_kv[1].strip()

        for args_list_item in args_list:
            if(arg_key == args_list_item):
                args_dict[arg_key] = arg_val
                break

    return args_dict



#####
#####               Print args dict
#####
def PrintArgsDict(args_dict, print_bool=True):
    if(print_bool != True):
        return

    print("\n<<ARGS DICT\n")
    for key, val in args_dict.items():
        print('\tkey: ' + key)
        print('\tval: ' + val)
        print('')
    print('ARGS DICT>>\n')
