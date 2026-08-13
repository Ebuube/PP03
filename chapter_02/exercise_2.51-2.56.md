### 2.51

What is the hexadecimal representation of the following numbers?

1. 25,675
= 0110 0100 0100 1011
= x644B

2. 675.625 (i.e., 675+5/8), in the IEEE 754 floating point standard
= 675 + 1/8 + 4/8
= 675 + 1/8 + 1/2
= 0010 1010 0011 + 0.101
= 0010 1010 0011.101
= 1.010100011101 * 2^9

In IEEE floating point format:

$= (-1)^S * 1.fraction * 2^E - 127$

S = 0 (positive)
fraction = 0.010100011101
E = 127 + 9 = 136

0 1000 1000 0101 0001 1101 0000 0000 000

=> 0100 0100 0010 1000 1110 1000 0000 0000

= x4428E800

3. The ASCII string: Hello
= H e l l o
= x48 65 6C 6C 6F
= x48656C6C6F

### 2.52

Consider two hexadecimal numbers: x434F4D50 and x55544552. What values do they represent for each of the five data types shown?

|   | x434F4D50 | x55544552 |
|:---:|:---:|:---:|
| Unsigned binary | 0100 0011 0100 1111 0100 1101 0101 0000 | 0101 0101 0101 0100 0100 0101 0101 0010 |
| 1's complement | 0100 0011 0100 1111 0100 1101 0101 0000 | 0101 0101 0101 0100 0100 0101 0101 0010 |
| IEEE 754 floating point | 0 1000 0001 0000 1101 0011 1101 0011 010  | 0 1001 1101 0101 0101 0101 0001 0001 010 |
| ASCII string | COMP | UTER |

### 2.53

Fill in the truth table for the equations given. The first line is done as an example.

Q1 = NOT(A AND B)
Q2 = NOT(NOT(A) AND NOT(B))

| A | B | Q1 | Q2 |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 |

### 2.54

Fill in the truth table for the equations given. The first line is done as an example.

Q1 = NOT(NOT(X) OR (X AND Y AND Z))
Q2 = NOT((Y OR Z) AND (X AND Y AND Z))


| X | Y | Z | Q1 | Q2 |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 |


### 2.55

We have represented numbers in base-2 (binary) and in base-16 (hex). We are now ready for unsigned base-4, which we will call quad numbers. A quad digit can be 0, 1, 2, or 3.

1. What is the maximum unsigned decimal value that one can represent with 3 quad digits?

It is $4^n - 1$ = 63

2. What is the maximum unsigned decimal value that one can represent with n quad digits? (Hint: Your answer should be a function of n.)

It is $4^n - 1$

3. Add the two unsigned quad numbers: 023 and 221.
```text
    023
+   221
-------
=   310
```

4. What is the quad representation of the decimal number 42?

= 200 + 20 + 2 = 222

5. What is the binary representation of the unsigned quad number 123.3?

$= 123 = 16 + 8 + 3 = 27_{10}$

$0.3_4$ = 3 * 1/4 = 0.75_{10}$

$27_{10} = 11011_2$

$0.75 => 0.5 + 0.25 = 1/2 + 1/4$

$0.75_2 = 0.11_2$

Therefore,

$123.3_4 = 11011.11_2$

6. Express the unsigned quad number 123.3 in IEEE floating point format.

$123.3_4 = 11011.11_2 = +1 * 1.101111 * 2^4$

Stored exponent = 4 + 127 = 131

In IEEE floating point format

= 0 1000 0011 1011 1100 0000 0000 0000 000

= 0100 0001 1101 1110 0000 0000 0000 0000

7. Given a black box that takes m quad digits as input and produces one quad digit for output, what is the maximum number of unique functions this black box can implement?

#### Solution

Not understood yet.

### 2.56

Define a new eight-bit floating point format with one sign bit, four bits of exponent, using an excess-7 code (i.e., the bias is 7), and three bits of fraction. If xE5 is the bit pattern for a number in this eight-bit floating point format, what value does it have? (Express as a decimal number.)

#### Solution

Sample: 1 1111 111

Sign bit (S) = 1
Exponent (E) = 1111 = 15
Fraction = 111 => 0.111

Definition
---

Format for 8-bit floating point

$(-1)^S * 1.fraction * 2^{E - 7}$

1. xE5 = 1110 0101 = 1 1100 101

S = 1
Fraction = 101 = 0.101
E = 1100 = 12

=> $(-1)^1 * 1.101 * 2^{12 - 7}$

= -1 * 1.101 * 2^5

$= -110100_2$

$= -52_{10}$
