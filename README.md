# GT_generator

## What is GT_generator
GT_generator helps generating ground truth for dhSegment. It intends to complete the last step of the creation of ground truth, as explained in [the documentation](https://dhsegment.readthedocs.io/en/latest/start/annotating.html).
scripts to create ground truth for dhsegment

## Requirements
This script requires the installation of:
- the [openCV python library](https://opencv.org/)
- [dhSegment](https://dhsegment.readthedocs.io/en/latest/index.html)

## How to run GT_generator
Following dhSegment tutorial, you will most likely end up, for a single annotated image, with multiple black and white masks (one per class of annotation). In order to create proper ground truth, you will need to color each mask according to their class and to combine these masks all together.

### 1. assign each class a color
In `class_color.py`, the variable `my_classes` stores information on each class:
- the name
- the associated **BGR** color
- a number corresponding to its z-order (similar to CSS's z-index)

``` python
my_classes = {
    "<name>":{
        "color": [<B-value>,<G-value>,<R-value>],
        "order": <z-order>}
}
```

### 2. color and combine masks
`combine_mask.py` uses information provided in `class_color.py` to organize layers in the desired order and assigne each new layer a color.

It takes up to three arguments:
- `-i`: is required, and provides the absolute path to the directory containing original mask images
- `-o`: is not required, and allows the user to specify the destination of the final in the form of an absolute path. Default output destination is `{input_path}/combined/combined.png`.
- `--test`: activates test mode which will display various informative messages during the execution of the script.

**WARNING** : masks are expected to have been created using the script provided as an example in [dhSegment documentation on annotation](https://github.com/dhlab-epfl/dhSegment/blob/04ce8b6db9a3fef3840c7fbbb8e65950851a3355/doc/start/annotating.rst), so the script will expect the name of the mask's class to be indicated in the name of the image file.

``` shell
python combine_mask.py -i path/to/input -o /path/to/output
```
