from PIL import Image


def grayscale(image):
    """
    Return a new image converted to grayscale.

    For each pixel, compute the luminance:
        gray = round(0.299 * r + 0.587 * g + 0.114 * b)
    Then set the pixel to (gray, gray, gray).
    """
    # TODO: implement
    pass


def invert(image):
    """
    Return a new image with every pixel inverted (photo negative).

    For each pixel, set it to (255 - r, 255 - g, 255 - b).
    """
    # TODO: implement
    pass


def mirror(image):
    """
    Return a new image flipped horizontally.

    The pixel at (x, y) in the output should be the pixel at
    (width - 1 - x, y) in the input.
    """
    # TODO: implement
    pass


def main():
    image = Image.open("cat.jpg").convert("RGB")

    grayscale(image).save("cat-gray.jpg")
    invert(image).save("cat-invert.jpg")
    mirror(image).save("cat-mirror.jpg")

    print("Saved cat-gray.jpg, cat-invert.jpg, cat-mirror.jpg")


if __name__ == "__main__":
    main()
