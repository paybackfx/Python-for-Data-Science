#!/usr/bin/env python3
# =============================================================================
# EXERCISE 04: ROTATE ME
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Transposing By Hand: the subject forbids any library helper, so the
#    output pixel (x, y) is read from the input pixel (y, x). A nested list
#    comprehension expresses exactly that swap of the two indices.
# 2. Transpose Is Not A Rotation: it mirrors the image along its main
#    diagonal. A true 90 degree rotation would additionally reverse one axis;
#    the subject asks for the transpose, so no axis is reversed.
# 3. Square Crop First: transposing a (h, w) image gives a (w, h) one, so
#    cutting a square keeps the shape stable at (400, 400) before and after.
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


def ft_transpose(matrix: list) -> list:
    """Return the transpose of a 2D list, swapping rows and columns."""
    height = len(matrix)
    width = len(matrix[0])
    return [[matrix[y][x] for y in range(height)] for x in range(width)]


def show(transposed: np.ndarray) -> None:
    """Display the transposed image with a pixel scale on both axes."""
    plt.imshow(transposed, cmap="gray")
    plt.title(f"Transpose of animal.jpeg - {SIZE}x{SIZE} pixels")
    plt.xlabel("x (pixels)")
    plt.ylabel("y (pixels)")
    plt.show()


def main() -> None:
    """Load animal.jpeg, cut a square, transpose it and display it."""
    array = ft_load("animal.jpeg")
    if array is None:
        return
    try:
        zoomed = zoom(array)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed)
    flat = zoomed[:, :, 0].tolist()
    transposed = np.array(ft_transpose(flat), dtype=np.uint8)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    show(transposed)


if __name__ == "__main__":
    main()
