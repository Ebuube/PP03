#!/usr/bin/env python3
"""
IEEE 754 Decoder for Floating point data type

Todo:
    []  Solve edge case of delimiter input being ','
    []  Create an encoder function to convert a decimal into
        a float point `encode_ieee754(num_decimal, delim='-')`

This program decodes IEE 754 floating point data binary representation into decimal value. It also returns properties about the number such as classification, string representation, etc.

How to Use
---
Input format as below:

<sign_bit><delimiter><exponent_bits><delimiter><fraction/mantissa_bits>,<delimiter>

Eg:
1-11111110-11111111111111111111111,-

Blank lines are allowed in batch file. Sample use cases:
----
$ # Interactive shell
$ ./ieee754.py
$
$ # Read from STDIN
$ cat batch_file | ./ieee754.py
$
$ # OR
$ echo "1-11111110-11111111111111111111111,-" | ./ieee754.py
$
$ # Read from redirected STDIN
$ ./ieee754.py < batch_file
$
$ # Inside Python shell or another python file
$ python3
Python 3.14.6 (main, Jun 11 2026, 00:00:00) [GCC 16.1.1 20260515 (Red Hat 16.1.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ieee754
>>> from pprint import pprint
>>> b = '0-11111110-11111111111111111111111'
>>> delimiter = '-'
>>> pprint(ieee754.decode_ieee754(b, delimiter))
{'classification': 'normalized',
 'delimiter': '-',
 'exponent': 127,
 'format_spec': 'IEEE 754 standard for 32-bit floating point data type',
 'fraction': 0.9999998807907104,
 'input': '0-11111110-11111111111111111111111',
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


def decode_ieee754(ieee_float: str, delim: str = '') -> IEEEResult | str:
    """
    Convert a 32-bit binary float to standard form in base10
    The binary float should be in IEEE 754 standard
    sign-exponentfield-fraction

    @ieee_float: raw string for binary representation using IEEE 754 Standard
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
    elif exp_bin == "00000000" and frac_dec == 0:
        # Evaluate zero
        num_str = f"{sign_str}1 × 0"
        num_val = ((-1) ** sign_val) * 0
        num_class = "zero"
    elif exp_bin == "00000000" and frac_dec != 0:
    # Evaluate subnormal numbers
        num_str = f"{sign_str}1 × {frac_dec} × 2 ^ -126"
        num_val = ((-1) ** sign_val) * frac_dec * (2 ** -126)
        num_class = "denormalized/subnormal"
    elif exp_bin == "11111111" and frac_dec == 0:
    # Evaluate infinities
        num_str = f"{sign_str}∞"
        num_val = float("-inf") if sign_val == True else float("inf")
        num_class = "infinities"
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
        "format_spec": "IEEE 754 standard for 32-bit floating point data type",
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
        IEEE 754 Standard
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
    print("""This program continuously converts IEEE floating point \
representation to its binary equivalent.
While entering IEEE floats, use this format:

<sign_bit><delimiter><exponent_bits><delimiter><fraction/mantissa_bits>,<delimiter>

Example
0-11111110-11111111111111111111111,-
Where '-' is the delimiter. A space can be the delimiter

You can also pass input from STDIN or redirected STDIN

$ ./ieee754.py < batch_file
$ cat batch_file | ./ieee754.py
$ echo 0-11111110-11111111111111111111111,- | ./ieee754.py
""")
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
        pprint(decode_ieee754(num, delim))
