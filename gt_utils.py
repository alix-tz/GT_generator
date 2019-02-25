import os
import cv2


def get_glimpse(image, wk=False):
    """ show a small overview of an image (10% of original size)

    :param img: image
    :param wk: true if waitkey active
    :return:
    """
    if wk is True:
        wktime = 0
    else:
        wktime = 50
    dim = (int(image.shape[1] * 0.1), int(image.shape[0] * 0.1))
    visible = resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("current image", visible)
    cv2.waitKey(wktime)
    return


def make_path_to_out(path_out, path_orig, default):
    """ validate abs path given by user or change it to default

    :param path_out: abs path to output (str)
    :param path_orig: abs path to input (str)
    :return:
    """
    if path_out:
        if not path_out.startswith("/"):
            print("invalid output path, images will be saved in {}".format(os.path.join(path_orig, default)))
            path_out = os.path.join(path_orig, default)
    else:
        path_out = os.path.join(path_orig, default)
    return path_out
