def rgb_to_hex(r, g, b):
    """
    Convert RGB integers (each 0-255) to a hex string like '#rrggbb'.

    Examples:
        rgb_to_hex(255, 0, 0)       -> '#ff0000'
        rgb_to_hex(0, 255, 0)       -> '#00ff00'
        rgb_to_hex(4, 30, 66)       -> '#041e42'

    Notes:
      - Use lowercase letters in the output.
      - Each channel must be padded to exactly two hex digits.
    """
    # TODO: implement
    pass


def hex_to_rgb(hex_str):
    """
    Convert a hex string to a tuple (r, g, b).

    Examples:
        hex_to_rgb('#ff0000')  -> (255, 0, 0)
        hex_to_rgb('ff0000')   -> (255, 0, 0)
        hex_to_rgb('#041e42')  -> (4, 30, 66)

    Notes:
      - The leading '#' is optional.
      - The input is always exactly 6 hex digits (plus optional '#').
      - You can assume the input is valid hex; you don't need to validate it
        here (that's what is_valid_rgb is for, after conversion).
    """
    # TODO: implement
    pass


def complement(r, g, b):
    """
    Return the complementary color: (255 - r, 255 - g, 255 - b).

    Examples:
        complement(255, 0, 0)   -> (0, 255, 255)   (red -> cyan)
        complement(0, 0, 0)     -> (255, 255, 255) (black -> white)
        complement(100, 100, 100) -> (155, 155, 155)
    """
    # TODO: implement
    pass


def is_valid_rgb(r, g, b):
    """
    Return True if all three values are integers in the inclusive range 0-255,
    False otherwise.

    Examples:
        is_valid_rgb(255, 0, 0)  -> True
        is_valid_rgb(0, 0, 0)    -> True
        is_valid_rgb(256, 0, 0)  -> False  (256 is too high)
        is_valid_rgb(-1, 0, 0)   -> False  (negative not allowed)
    """
    # TODO: implement
    pass
