"""
Utilities functions for interconverting number representation
"""
import re

def bin_to_dec(binary: str, delim: str = '') -> str:
    """
    Convert a 32-bit binary float to standard form in base10
    The binary float should be in IEEE 745 standard
    sign-exponentfield-fraction

    @binary: raw string for binary representation using IEEE 745 Standard
    @delim: user's choice of delimiter
    Return: string for standard form in base10
    """
    float_t = re.compile(
        rf'([01]){re.escape(delim)}([01]{{8}}){re.escape(delim)}([01]{{23}})'
    )

    match = float_t.fullmatch(binary)

    if not match:
        print("Invalid format")
        return ''

    sign_bin = match.group(1)
    exp_bin = match.group(2)
    frac_bin = match.group(3)

    sign_str = '-' if int(sign_bin, 2) else '+'
    exp_dec = get_exponent(exp_bin)
    frac_dec = get_fraction(frac_bin)

    # Evaluate full number
    if exp_dec not in (-126, 255):
        num_str = f"{sign_str}1 x {1+frac_dec} x 2 ^ {exp_dec}"
        return num_str

    # Evaluate infinities
    if exp_dec == 255:
        num_str = f"{sign_str}∞"
        return num_str

    # Evaluate subnormal numbers
    if exp_dec == -126:
        num_str = f"{sign_str}1 x {frac_dec} x 2 ^ -126"
        return num_str


def get_fraction(frac: str) -> float:
    """
    Get the decimal value of the fraction/mantissa part of
    a 32-bit float point data type

    @frac: 23-bit binary representation of fraction field
    """
    val = sum(
        int(bit) * 2 ** -(i + 1)
        for i, bit in enumerate(frac)
    )
    return val


def get_exponent(exp: str) -> int:
    """
    Get the decimal value of the exponent using 127 as the bias
    
    @exp: 8-bit binary representation of exponen according to
        IEEE 745 Standard
    """
    # Special exponents
    ZERO = '00000000'
    INFINITY = '11111111'

    if exp == ZERO:
        return -126     # Subnormal/denormalized number's exponent
    elif exp == INFINITY:
        return 255
    else:
        return int(exp, 2) - 127
