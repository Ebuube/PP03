#!/usr/bin/env python3
"""
Utilities functions for interconverting number representation

Todo:
    - Create classification for -0.0 and +0.0 named 'zero'
    - Read from batch file containing: <num>,<delimiter>
    - Solve edge case of delimiter input being ','

How to Use
----
>>> from pprint import pprint
>>> import num
>>> b = '0 11111110 11111111111111111111111'
>>> pprint(num.decode_ieee745(b, delim=' '))
{'classification': 'normalized',
 'exponent': 127,
 'format_spec': 'IEEE 745 standard for 32-bit floating point data type',
 'fraction': 0.9999998807907104,
 'input': '0 11111110 11111111111111111111111',
 'sign': 0,
 'string': '+1 × 1.9999998807907104 × 2 ^ 127',
 'value': 3.4028234663852886e+38}
>>> 
"""
import re

from typing import TypedDict
from pprint import pprint


class IEEEResult(TypedDict):
    input: str
    sign: int
    exponent: int
    fraction: float
    value: float
    string: str
    delimiter: str
    classification: str
    format_spec: str


def decode_ieee745(ieee_float: str, delim: str = '') -> IEEEResult | str:
    """
    Convert a 32-bit binary float to standard form in base10
    The binary float should be in IEEE 745 standard
    sign-exponentfield-fraction

    @ieee_float: raw string for binary representation using IEEE 745 Standard
    @delim: user's choice of delimiter
    Return: IEEEResult dictionary of decoded values or '' if invalid
    """
    float_t = re.compile(
        rf'([01]){re.escape(delim)}([01]{{8}}){re.escape(delim)}([01]{{23}})'
    )

    match = float_t.fullmatch(ieee_float)

    if not match:
        print("Invalid format")
        return ''

    sign_bin = match.group(1)
    exp_bin = match.group(2)
    frac_bin = match.group(3)

    sign_val = int(sign_bin, 2)
    sign_str = '-' if sign_val == True else '+'
    exp_dec = get_exponent(exp_bin)
    frac_dec = get_fraction(frac_bin)

    # Evaluate full number
    if exp_bin not in ("00000000", "11111111"):
        num_str = f"{sign_str}1 × {1+frac_dec} × 2 ^ {exp_dec}"
        num_val = ((-1) ** sign_val) * (1 + frac_dec) * (2 ** exp_dec)
        num_class = "normalized"
    elif exp_bin == "11111111" and exp_dec == 0:
    # Evaluate infinities
        num_str = f"{sign_str}∞"
        num_val = float("-inf") if sign_val == True else float("inf")
        num_class = "infinities"
    elif exp_bin == "00000000":
    # Evaluate subnormal numbers
        num_str = f"{sign_str}1 × {frac_dec} × 2 ^ -126"
        num_val = ((-1) ** sign_val) * frac_dec * (2 ** -126)
        num_class = "denormalized/subnormal"
    else:
        num_str = "Not a Number"
        num_val = float("nan")
        num_class = "NaN"

    return {
        "input": ieee_float,
        "delimiter": delim,
        "sign": sign_val,
        "exponent": exp_dec,
        "fraction": frac_dec,
        "value": num_val,
        "string": num_str,
        "classification": num_class,
        "format_spec": "IEEE 745 standard for 32-bit floating point data type",
    }


def get_fraction(frac: str) -> float:
    """
    Get the decimal value of the fraction/mantissa part of
    a 32-bit floating point data type

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

if __name__ == "__main__":
    print("""This program continuosly converts IEEE floating point \
representation to its binary equivalent. Eg. 1 10000001 10101000000000000000000
While entering IEEE floats, use this format: <num>,<delimiter>
0 11111110 11111111111111111111111,-
Where '-' is the delimiter. A space can be the delimiter""")
    msg = "This is the end... Hold your breath and count to ten.."

    while True:
        try:
            data = input("Enter IEEE float: ")
            data = [item for item in data.split(sep=',')]
            num = data[0].strip()
            try:
                delim = data[1]
            except IndexError:
                delim = ''
        except (KeyboardInterrupt, EOFError):
            print(msg)
            break
        if not num:
            continue
        pprint(decode_ieee745(num, delim))
