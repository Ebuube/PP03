Date: Tue  4 Aug 00:31:59 WAT 2026

6-bit 2's complement binary representation
---
3<sub>10</sub> = 000011<sub>2</sub>

-3<sub>10</sub> = 111101<sub>2</sub>

-5<sub>10</sub> = 111011<sub>2</sub>

(- 3) + (- 5)

```text
    111101
+   111011
----------
    111000
```

111000<sub>2</sub> = -8<sub>10</sub>

Bitwisie Logical Operations
---

### 1st DeMorgan's Law

`~(~A AND ~B) = A OR B`

| A | B | ~A | ~B | ~(~A AND ~B) | A OR B |
|:-:|:-:|:--:|:--:|:------------:|:------:|
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 |

### Experiment

What happens if one inverts both inputs to an OR function, then inverts the output?

| A | B | ~A | ~B | ~(~A OR ~B) | A AND B |
|:-:|:-:|:--:|:--:|:-----------:|:-------:|
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 |

The table above expresses the 2nd DeMorgan's Law:
`~(~A OR ~B) = A AND B`

### Example 2.12

What does the floating point data type

*a*<sub>10</sub> = 00111101100000000000000000000000<sub>2</sub>

represent?

#### Solution

Break the number to expose the three fields: sign, exponent and fraction fields.

Sign (S) - Exponent - Fraction

0-01111011-00000000000000000000000

Normalized form binary representation says

-1<sup>S</sup> * 1.fraction * 2<sup>exponent - 127</sup>, 1 <= exponent <= 254

For the number *a*:

S = 0 i.e. positive sign

exponent field = 01111011<sub>2</sub> = 123<sub>10</sub>

fraction field = 00000000000000000000000<sub>2</sub> = 0<sub>10</sub>

Therefore:
*a*<sub>10</sub> = -1<sup>0</sup> * 1.0 * 2<sup>123 - 127</sup>

= 1 * 1.0 * 2<sup>-4</sup>

*a*<sub>10</sub>= 0.0625

### Example 2.13

How is the number -6<sup>5</sup>/<sub>8</sub> represented in the floating point data type?

#### Solution

*a*<sub>10</sub> = -6<sup>5</sup>/<sub>8</sub>

= -6 + 5/8 = -6 + (1/8 + 4/8)

Sign is negative

binary for 6 = 110

binary for 1/8 = 0.001

binary for 4/8 = 1/2 = 0.1

binary for 5/8 = 0.101

binary for +6 + 5/8 = 110.101 = 1.10101⋅2<sup>2</sup>

Putting in normalized form

Sign (S) - Exponent - Fraction

0-00000000-00000000000000000000000

**S** = 1 i.e. negative number

**Exponent** = 2
Add 127 bias = 129 = 10000001<sub>2</sub> (unsigned)

Main number = 1.10101

But we have to discard the leading 1' bit since it is the only possible non-zero digit and we can always put it back on reconversion

Therefore,

**Fraction** = 10101 <sub>2</sub>

Therefore final representation

1-10000001-10101

Add trailing zeros to the fraction to complete the 23 bit representation

1 10000001 10101000000000000000000

Putting everything together: decimal to float point data type

-6<sup>5</sup>/<sub>8</sub> = 1 10000001 10101000000000000000000

### Other examples of Floating point numbers

1. 0 10000011 00101000000000000000000 is 1.00101 ⋅ 2^4 = 18.5

2. 1 10000010 00101000000000000000000 is 1.00101 ⋅ 2^3 = -9.25

3. 0 11111110 11111111111111111111111 is 1.111111 ⋅ 2^(254-127)
```text
 1.111111 approx 2

 i.e 2 ⋅ 2^127 = 2^128
```

smallestNormalizedNum - smallestSubNormalizedNum = largestNormalizedNum

### Test of Knowledge

What number corresponds to the following ﬂoating point representation?

0 00000000 00001000000000000000000

#### Solution

Sign - Exponent Field - Fraction

Sign = S = 0

Exponent Field = 00000000

This Field pattern is for denormalized numbers and it gives E the value -126

E = -126

Fraction

Since, we are dealing with a denormalized number, the first leading digit is 0. So, no implicit leading 1 digit

0.00001<sub>2</sub>

= 1.0 * 2<sup>-5</sup>

Putting the exponent, -126

=> 1.0 * 2<sup>-5</sup> * 2 <sup>-126</sup>

S is 0 thus it is a positive number

=> 1.0 * 2<sup>-131</sup>

= 2<sup>-131</sup>


### Infinities

+infinity = 0 11111111 00000000000000000000000

-infinity = 1 11111111 00000000000000000000000

### Subnormal/Denormalized numbers

All the bits in the exponent field is all set to `0`. And the exponent is always the value `-126`. There is no implicit 1. This means we only have 23-bit precision when representing denormalized numbers.

The sign bit retains its meaning. i.e. 1 means negative number, 0 means positive number.

The fraction field (mantissa) is intrepreted as `0.fraction`.

So, the subnormal/denormalized numbers are expressed as

-1<sup>S</sup> * 0.fraction * 2<sup>-126</sup>

Example: 0 00000000 00001000000000000000000 is a denormalized number.

Sign bit is 0 => positive number

Exponent field: all 8 bits are 0 thus, it is a denormalized number.

Fraction field = 00001

Putting it all together

base<sup>10</sup> repr = -1<sup>0</sup> * 0.00001 * 2<sup>-126</sup>

= 2<sup>-131</sup>
