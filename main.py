import cv2 as cv


def pixelation_pictures(img, pix):
    """
    function takes an image or part
    of it and turns it into a pixelated image
    pix - single pixel size

    :param img, pix:
    :return new pixelated image:
    """
    x = 0  # start for pixelation x
    y = 0  # start for pixelation y
    py, px, _ = img.shape  # photo size

    px -= (px % pix)  # preparation for processing x
    py -= (py % pix)  # preparation for processing y

    img = cv.resize(img, (px, py))  # photo resizing for correct processing

    while y < img.shape[0]:  # photo pixelation
        while x < img.shape[1]:
            b = img[y + pix // 2, x + pix // 2]
            img[y: y + pix, x: x + pix] = b
            x += pix
        x = 0
        y += pix

    # cv.imshow('res', img)  # show img
    # cv.waitKey(0)

    return img  # return new image
