#!/usr/bin/env python3
# =============================================================================
# EXERCISE 05: PIMP MY IMAGE
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Restricted Operators: the subject allows a different operator set per
#    filter, so each one is written with those only - invert uses "-", red
#    uses "*", green subtracts a channel from itself to zero it, blue simply
#    assigns 0, and grey copies one channel over the other two.
# 2. .copy() Is Mandatory: NumPy slicing returns a view, so writing into a
#    slice of the argument would silently corrupt the caller's image. Every
#    filter works on its own copy and the original array stays intact.
# 3. The Shape Never Changes: all five filters return a (h, w, 3) array, so
#    they can be chained or compared side by side without any reshaping.
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = array.copy()
    inverted = 255 - inverted
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Turns the image received into shades of grey."""
    grey = array.copy()
    grey[:, :, 0] = grey[:, :, 1]
    grey[:, :, 2] = grey[:, :, 1]
    return grey


def show_filters(array: np.ndarray) -> None:
    """Display the original image next to the five filtered versions."""
    panels = [
        ("Original", array),
        ("Invert", ft_invert(array)),
        ("Red", ft_red(array)),
        ("Green", ft_green(array)),
        ("Blue", ft_blue(array)),
        ("Grey", ft_grey(array)),
    ]
    figure, axes = plt.subplots(2, 3, figsize=(12, 6))
    figure.suptitle("Pimp my image - landscape.jpg")
    for axis, (title, image) in zip(axes.ravel(), panels):
        axis.imshow(image)
        axis.set_title(title)
        axis.set_xlabel("x (pixels)")
        axis.set_ylabel("y (pixels)")
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Load landscape.jpg and display the five color filters applied."""
    array = ft_load("landscape.jpg")
    if array is None:
        return
    print(array)
    show_filters(array)


if __name__ == "__main__":
    main()
