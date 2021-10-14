# Implementation of the Gaborfilter
# https://en.wikipedia.org/wiki/Gabor_filter
import numpy as np
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, filter2D, CV_8UC3, imshow, waitKey


def gabor_filter_kernel(
    ksize: int, sigma: int, theta: int, lambd: int, gamma: int, psi: int
) -> np.ndarray:
    """
    :param ksize:   The kernelsize of the convolutional filter (ksize x ksize)
    :param sigma:   standard deviation of the gaussian bell curve
    :param theta:   The orientation of the normal to the parallel stripes
                    of Gabor function.
    :param lambd:   Wavelength of the sinusoidal component.
    :param gamma:   The spatial aspect ratio and specifies the ellipticity
                    of the support of Gabor function.
    :param psi:     The phase offset of the sinusoidal function.
    """

    # prepare kernel
    gabor = np.zeros((ksize, ksize), dtype=np.float32)

    # each value
    for y in range(ksize):
        for x in range(ksize):
            # distance from center
            px = x - ksize // 2
            py = y - ksize // 2

            # get kernel x
            _x = np.cos(theta) * px + np.sin(theta) * py

            # get kernel y
            _y = -np.sin(theta) * px + np.cos(theta) * py

            # fill kernel
            gabor[y, x] = np.exp(
                -(_x ** 2 + gamma ** 2 * _y ** 2) / (2 * sigma ** 2)
            ) * np.cos(2 * np.pi * _x / lambd + psi)

    return gabor


if __name__ == "__main__":
    # read original image
    img = imread("../image_data/lena.jpg")
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # Apply multiple Kernel to detect edges
    out = np.zeros(gray.shape[:2])
    for theta in [0, 30, 60, 90, 120, 150]:
        """
        ksize = 10
        sigma = 8
        lambd = 10
        gamma = 0
        psi = 0
        """
        kernel_10 = gabor_filter_kernel(10, 8, theta, 10, 0, 0)
        out += filter2D(gray, CV_8UC3, kernel_10)
    out = out / out.max() * 255
    out = out.astype(np.uint8)

    imshow("original", gray)
    imshow("gabor filter with 20x20 mask and 6 directions", out)

    waitKey(0)
