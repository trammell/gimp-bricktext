#!/usr/bin/env python

from gimpfu import *

def bricktext(img, layer) :
    # Actual plug-in code will go here
    pdb.gimp_image_flip(img, ORIENTATION_VERTICAL)
    return

register(
    "python_fu_bricktext",
    "Creates LEGO(C) text",
    "Creates LEGO(C) text",
    "John Trammell <johntrammell@gmail.com>",
    "John Trammell <johntrammell@gmail.com>",
    "2012",
    "Brick Text",
    "",         # "*"
    [   # parameters
    ],
    [], # return values
    bricktext,
    menu="/Filters/Distorts")

