#!/usr/bin/env python3
# =============================================================================
# EXERCISE 03: ZOOM ON ME
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Two-Dimensional Slicing (array[y0:y1, x0:x1]): rows come first because
#    the array is indexed (height, width, channels). Cropping is therefore a
#    view expressed in pixel coordinates, not a resize.
# 2. Luminance, Not Average: the eye is far more sensitive to green than to
#    blue, so the greyscale value is 0.299 R + 0.587 G + 0.114 B rather than
#    a plain mean of the three channels.
# 3. Keeping The Channel Axis (np.newaxis): the subject asks for a
#    (400, 400, 1) array, so a third axis of size one is added back after the
#    channels have been collapsed into a single luminance value.
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load

TOP = 284
LEFT = 187
SIZE = 400


def zoom(array: np.ndarray) -> np.ndarray:
    """Return a SIZE x SIZE single channel crop of the given image."""
    if TOP + SIZE > array.shape[0] or LEFT + SIZE > array.shape[1]:
        raise ValueError("the zoom area does not fit inside the image")
    crop = array[TOP:TOP + SIZE, LEFT:LEFT + SIZE]
    luminance = (0.299 * crop[:, :, 0]
                 + 0.587 * crop[:, :, 1]
                 + 0.114 * crop[:, :, 2])
    return luminance.astype(np.uint8)[:, :, np.newaxis]


def show(zoomed: np.ndarray) -> None:
    """Display the zoomed image with a pixel scale on both axes."""
    plt.imshow(zoomed[:, :, 0], cmap="gray")
    plt.title(f"Zoom on animal.jpeg - {SIZE}x{SIZE} pixels")
    plt.xlabel("x (pixels)")
    plt.ylabel("y (pixels)")
    plt.show()


def main() -> None:
    """Load animal.jpeg, print it, then display the zoomed grey crop."""
    array = ft_load("animal.jpeg")
    if array is None:
        return
    print(array)
    try:
        zoomed = zoom(array)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)
    show(zoomed)


if __name__ == "__main__":
    main()
