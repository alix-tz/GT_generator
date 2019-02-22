import itertools
import cv2
import os
import time
import numpy as np
import gt_utils
import gt_io as io

import argparse

from class_colors import my_classes
# additional features :
# - verify image format
# - order layers depending on the values of my_classes[key][order]

def combine(bg, fg):
    for y, x in itertools.product(range(fg.shape[0]), range(fg.shape[1])):
        if np.sum(fg[y, x]):
            bg[y, x] = fg[y, x]
    return bg

start = time.time()

ap = argparse.ArgumentParser(description="combine several RGB images in a directory")
ap.add_argument("-i","--input", required=True, help="absolute path to the repository containing images")
ap.add_argument("-o", "--output", help="absolute path to repository receiving resulting file, default is 'combined/' in initial repository")
ap.add_argument("--test", action="store_true", help="activate test mode")
args= vars(ap.parse_args())

if args["test"] is True:
    print(args)

PATH_TO_IMG_ORIG = args["input"]
PATH_TO_IMG_OUT = gt_utils.make_path_to_out(args["output"],PATH_TO_IMG_ORIG)
os.makedirs(PATH_TO_IMG_OUT, exist_ok=True)
if args["test"] is True:
    print("taken from: {}".format(PATH_TO_IMG_ORIG))
    print("saved to: {}".format(PATH_TO_IMG_OUT))

layers = io.get_layers(PATH_TO_IMG_ORIG)
if args["test"] is True:
    print("will process: {} files\n{}".format(len(layers), layers))

images = []
for layer in layers:
    image = cv2.imread(os.path.join(PATH_TO_IMG_ORIG, layer))
    images.append(image)
if args["test"] is True:
    print(len(images))

canvas = np.zeros(images[0].shape, dtype='uint8')
if args["test"] is True:
    print(canvas.shape)

bg = canvas
for img in images:
    bg = combine(bg,img)

end = time.time()
print(end-start)
if args["test"] is True:
    gt_utils.get_glimpse(bg, wk=False)

combined_img_name = os.path.basename(os.path.normpath(PATH_TO_IMG_ORIG)) + ".png"
print("combination saved as {}".format(combined_img_name))
cv2.imwrite(os.path.join(PATH_TO_IMG_OUT, combined_img_name), image)

