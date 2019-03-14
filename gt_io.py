import os
from class_colors import my_classes

CLASS_NAMES = list(my_classes.keys())

def get_originals(loc):
    """ explore a repository and get image file names eligible to transformation

    :param loc: path to the repository contening files (str)
    :return: list of image file names to transform (without path)
    """
    # migh tbe useful to add a test on whether or not the file is compatible with image transformation (tiff, png, jpg...)
    try:
        rep_content = os.listdir(loc)
        if len(rep_content) == 0:
            return False
        else:
            rep_content[:] = (f for f in rep_content if f != ".DS_Store")
            rep_content[:] = (f for f in rep_content if f != "processed")
            rep_content[:] = (f for f in rep_content if f != "combined")
            rep_files = []
            for f in rep_content:
                complete_path_to_f = os.path.join(loc, f)
                if os.path.isfile(complete_path_to_f):
                    rep_files.append(f)
            originals = []
            for f in rep_files:
                for c in CLASS_NAMES:
                    if c in f:
                        originals.append(f)
            return originals
    except Exception as e:
        print(e)
        return []


def get_layers(loc):
    """ explore a repository and get image file names containing layers

    :param loc: path to the repository contening files (str)
    :return: list of image file names to transform (without path)
    """
    # migh tbe useful to add a test on whether or not the file is compatible with image transformation (tiff, png, jpg...)
    try:
        rep_content = os.listdir(loc)
        if len(rep_content) == 0:
            return False
        else:
            rep_content[:] = (f for f in rep_content if f != ".DS_Store")
            layers = []
            for f in rep_content:
                complete_path_to_f = os.path.join(loc, f)
                if os.path.isfile(complete_path_to_f):
                    layers.append(f)
            return layers
    except Exception as e:
        print(e)
        return []


def get_class_color(filename):
    """ assign a class of mask to an image file, assuming the class is contained within the file name

    :param files: file name (str)
    :return: mask class (str), mask BRG code (list)
    """
    for c in CLASS_NAMES:
        if c in filename:
            return c, my_classes[c]["color"]
    # default is RED
    return "default", [0,0,255]


def get_class_order():
    """ calculate layers' order from user's indications in class_color.py

    :return: list of class names where first item is the bottom layer and last item is the top layer
    """
    theorder = [my_classes[type]["order"] for type in my_classes]
    theorder.sort()
    ordered_classes = []
    for o in theorder:
        for type in my_classes:
            if int(my_classes[type]["order"]) == int(o):
                ordered_classes.append(type)
    return ordered_classes