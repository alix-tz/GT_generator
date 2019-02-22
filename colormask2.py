import os
import cv2
import numpy as np
import gt_io as io
import gt_utils
import argparse

ap = argparse.ArgumentParser(description="transform white mask to colored mask according to its class")
ap.add_argument("-i","--input", required=True, help="absolute path to the repository containing masks")
ap.add_argument("-o", "--output", help="absolute path to repository receiving new files, default is 'processed/' in initial repository")
ap.add_argument("--test", action="store_true", help="activate test mode")
args= vars(ap.parse_args())

if args["test"] is True:
    print(args)

PATH_TO_IMG_ORIG = args["input"]
if args["output"]:
    if args["output"].startswith("/"):
        PATH_TO_IMG_OUT = args["output"]
    else:
        print("invalid output path, images will be saved in {}".format(os.path.join(PATH_TO_IMG_ORIG, "processed")))
        PATH_TO_IMG_OUT = os.path.join(PATH_TO_IMG_ORIG, "processed")
else:
    PATH_TO_IMG_OUT = os.path.join(PATH_TO_IMG_ORIG, "processed")
if args["test"] is True:
    print("taken from: {}".format(PATH_TO_IMG_ORIG))
    print("saved to: {}".format(PATH_TO_IMG_OUT))

os.makedirs(PATH_TO_IMG_OUT, exist_ok=True)

originals = io.get_originals(PATH_TO_IMG_ORIG)
if args["test"] is True:
    print("will process: {} files\n{}".format(len(originals), originals))

for f in originals:
    thatclass, thatcolor = io.get_class_color(f)
    if args["test"] is True:
        print("{} = {}".format(thatclass, thatcolor))

    # load image
    image = cv2.imread(os.path.join(PATH_TO_IMG_ORIG, f))
    if args["test"] is True:
        gt_utils.get_glimpse(image)

    # change white [255,255,255] to desired color
    image[np.where((image == [255, 255, 255]).all(axis=2))] = thatcolor
    if args["test"] is True:
        gt_utils.get_glimpse(image)

    cv2.imwrite(os.path.join(PATH_TO_IMG_OUT, f), image)