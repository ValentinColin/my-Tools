""" Logical AND (&):
bit-by-bit comparison using logical AND
Example:
a = 92    # 01011100
b = 21    # 00010101
c = a & b # 00010100
ou
d = 92    # 01011100
e = 1     # 00000001
f = d & e # 00000000
"""


def udec2bin(dec_number: int, bins: int = 0) -> str:
    """Return a binary's string representation of the interger: dec_number.
    Complete left with zeros.
    """
    if dec_number == 0:
        bin_string = "0"
    else:
        bin_string = ""
        while dec_number != 0:
            # "01"[0] gives "0" AND "01"[1] gives "1"
            bin_string = "01"[dec_number & 1] + bin_string

            # Opérator '>>' (shift to the right = division by 2)
            dec_number = dec_number >> 1
    return bin_string.zfill(bins)


def dec2bin(dec_number: int, bins: int = 8) -> str:
    """Return a representation of any integer in a binary string."""
    if dec_number == 0:
        return "0".zfill(bins)
    if dec_number < 0:
        dec_number += 1 << bins
    bin_string = ""
    while dec_number != 0:
        dec_number, r = divmod(dec_number, 2)
        bin_string = "01"[r] + bin_string
    return bin_string.zfill(bins)


if __name__ == '__main__':
    n = 13
    max_bins = 8

    print(f"udec2bin {n}: {udec2bin(n):>{max_bins}}")
    print(f"dec2bin  {n}: {dec2bin(n):>{max_bins}}")

    n = -13

    print(f"dec2bin {n}: {dec2bin(n):>{max_bins}}")
