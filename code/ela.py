from __future__ import print_function
from PIL import Image, ImageChops, ImageEnhance
import os
import numpy as np

def ela(image_path):
    """
    Generates an ELA image on save_dir.
    Params:
        fname:      filename w/out path
        orig_dir:   origin path
        save_dir:   save path
    """
    im = Image.open(image_path)
    im.save("temp", 'JPEG', quality=95)

    tmp_fname_im = Image.open("temp")
    ela_im = ImageChops.difference(im, ImageChops.invert(tmp_fname_im))

    os.remove("temp")

    return np.array(ela_im)

    # ela_im.save("ela_image2.jpg")