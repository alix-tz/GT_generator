import itertools
import cv2
import os
import time
import numpy as np
import gt_utils
import gt_image
import gt_io as io


import argparse

# additional features :
# - verify image format

def order_layer(filenames):
    """ order file names in layer order assuming layer in given in file name
    warning: this operation will fail if classes are ambiguous. ex: 2 classes named "text" and "textzone".
    warning: this operation will fail if classes are not specific enough. ex: 2 classes names "a" and "b".

    :param filenames: list of filenames
    :return: list of ordered filenames or unchanged list of filenames
    """
    ordered_filenames = []
    classes = io.get_class_order()
    for c in classes:
        for f in filenames:
            if c in f:
                ordered_filenames.append(f)
    if len(filenames) == len(ordered_filenames):
        return ordered_filenames
    else:
        print("failed to calculate layer order")
        return filenames


start = time.time()

ap = argparse.ArgumentParser(description="combine several RGB images in a directory")
ap.add_argument("-i","--input", required=True, help="absolute path to the repository containing images")
ap.add_argument("-o", "--output", help="absolute path to repository receiving resulting file, default is 'combined/' in initial repository")
ap.add_argument("--test", action="store_true", help="activate test mode")
args= vars(ap.parse_args())

if args["test"] is True:
    print(args)

PATH_TO_IMG_ORIG = args["input"]
PATH_TO_IMG_OUT = gt_utils.make_path_to_out(args["output"],PATH_TO_IMG_ORIG, "combined")
os.makedirs(PATH_TO_IMG_OUT, exist_ok=True)
if args["test"] is True:
    print("taken from: {}".format(PATH_TO_IMG_ORIG))
    print("saved to: {}".format(PATH_TO_IMG_OUT))

layers = io.get_layers(PATH_TO_IMG_ORIG)
if args["test"] is True:
    print("will process: {} files\nnot ordered layers: {}".format(len(layers), layers))

layers = order_layer(layers)
if args["test"] is True:
    print("ordered layers: {}".format(layers))

colors = []
for layer in layers:
    thatclass, thatcolor = io.get_class_color(layer)
    colors.append(thatcolor)
    if args["test"] is True:
        print("{} = {}".format(thatclass, thatcolor))
if args["test"] is True:
    print("layer(s)'s color(s) = {}".format(colors))

images = []
for layer in layers:
    image = cv2.imread(os.path.join(PATH_TO_IMG_ORIG, layer))
    images.append(image)
if args["test"] is True:
    print("gathered: {} images".format(len(images)))

if args["test"] is True:
    canvas = np.zeros(images[0].shape, dtype='uint8')
    print("canvas will be (y,x,depth): {}".format(canvas.shape))

annotated_image = gt_image.makeannotatedimage(images, colors)

end = time.time()
print("execution time : {} seconds.".format(end-start))
if args["test"] is True:
    gt_utils.get_glimpse(annotated_image, wk=False, legend="final_image")

# this calculation of filename should probably be improved
combined_img_name = os.path.basename(os.path.normpath(PATH_TO_IMG_ORIG)) + ".png"
print("combination saved as {}".format(combined_img_name))
cv2.imwrite(os.path.join(PATH_TO_IMG_OUT, combined_img_name), annotated_image)

