"""
Package: core
Authors: Matej Hrabal
About: Argument parser
"""


import sys, os

# Checks number of args
def check_args(argv):
    if (len(argv) != 3):
        print("Usage: python3 Path_to_TIFF Path_to_CSV\n")
        exit()

# Gets TIFF file from args
def get_path_img(argv):
    check_args(argv)
    if (os.path.exists(argv[1])):
        return argv[1]
    else:
        print("Usage: python3 Path_to_TIFF Path_to_CSV\n")
        exit()

# Gets CSV from args
def get_path_csv(argv):
    open(argv[2], "w+")
    return argv[2]







