#!/usr/bin/env python3
# =============================================================================
# EXERCISE 02: LOAD MY IMAGE
# =============================================================================
# Educational Notes for Beginners:
#
# 1. An Image Is A 3D Array: Pillow decodes the JPEG and NumPy exposes it as
#    (height, width, channels) - note that height comes first, which is the
#    opposite of the (width, height) order Pillow reports in image.size.
# 2. convert("RGB"): a JPEG can be greyscale or CMYK, so the pixels are
#    normalised to three channels before conversion. The array then always
#    has a third dimension of size 3, whatever the source file was.
# 3. Errors Are Reported, Never Raised: the subject invalidates any uncaught
#    exception, so a missing file or an unsupported format prints a clear
#    message and returns None instead of propagating a traceback.
# =============================================================================

import sys

import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Print the shape of the JPEG at path and return its RGB pixel array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        with Image.open(path) as image:
            if image.format not in ("JPEG", "JPG"):
                raise ValueError(f"{path}: unsupported format "
                                 f"{image.format}, only JPG and JPEG")
            array = np.array(image.convert("RGB"))
    except FileNotFoundError:
        print(f"Error: {path}: no such file or directory")
        return None
    except UnidentifiedImageError:
        print(f"Error: {path}: not a readable image")
        return None
    except (TypeError, ValueError, OSError) as error:
        print(f"Error: {error}")
        return None
    print(f"The shape of image is: {array.shape}")
    return array


def main() -> None:
    """Load the image given on the command line and print its pixels."""
    if len(sys.argv) != 2:
        print("Usage: python load_image.py <image.jpg>")
        return
    print(ft_load(sys.argv[1]))


if __name__ == "__main__":
    main()
