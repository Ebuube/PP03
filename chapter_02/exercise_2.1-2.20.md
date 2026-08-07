### 2.1

|   Number of bits(n)   |   Number of possible combinations |
|:---------------------:|:---------------------------------:|
|   0   |   0   |
|   1   |   2   |
|   2   |   4   |
|   3   |   8   |
|   n   | 2<sup>n</sup> |

Therefore, given *n* bits, we can repesent 2<sup>n</sup> distinct combinations.

### 2.2

26 combinations

n ~= log<sub>2</sub>26

4 < n < 5

Therefore, the minimum number of bits reqruired to represent the 26 character alphabet is 5 bits.

To distinguish between uppper and lowercase version we need (26 * 2) distinct representations.

n ~= log<sub>2</sub>52

5 < n < 6

Therefore, to represent the 52 character alphabet will reqruire at least 6 bits.

Proper formula: To represent an alphabet with *n* different characters, the least number of bits required, *x* is

x = $\lceil log_2(n) \rceil$

### 2.3

1. For 400 different students we need = $\lceil log_2(400) \rceil$ = 9. So we need 9 bits.
2. 9 bits is enough for 512 students. So extra 112 students can be admitted.

### 2.4

Given *n* bits we can represent **$2^n$** unsigned integers in the range 0 to $2^n$ - 1

### 2.5

Using 5 bits to represent 7 and -7

|   Representation  |   7   |   -7  |
|:---:|:---:|:---:|
| 1's complement | 00111 | 11000 |
| signed magnitude | 00111 | 10111 |
| 2's complement | 00111 | 11001 |

### 2.6

6 bits 2's complement representation of -32.

0 = 000000

32 = 010000

-32 = 110000

### 2.7

Create a table showing the decimal values of all four-bit 2’s complement
numbers.

$2^4$ = 16. So our range is from $-2^{4-1}$ to $+2^{4-1} - 1$. That is -8 to +7.

| 4-bit number | Decimal value |
|:---:|:---:|
| 1000 | -8 |
| 1001 | -7 |
| 1010 | -6 |
| 1011 | -5 |
| 1100 | -4 |
| 1101 | -3 |
| 1110 | -2 |
| 1111 | -1 |
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |
| 0101 | 5 |
| 0110 | 6 |
| 0111 | 7 |

### 2.8

1. $2^8$ = 256. i.e from -128 to +127. So the largest positive number is $127_{10}$ also $0111111_2$.
2. It will be $-128_{10}$ also $1000000_2$.
3. In *n* bit 2's complement code, the largest positive number is $2^{n-1} - 1$.
4. $2^{n-1}$ is the greatest magnitude negative number in an *n*-bit 2's complement binary representation.

### 2.9

How many bits are needed to represent Avogadro’s number (6.02 ⋅ 1023 )
in 2’s complement binary representation?

#### Solution

Given a number *+A*. If it were to be the max number in its range, the range would be

-(A+1) to +A

Total numbers needed would be: $\lvert -(A + 1) \rvert + 1 + A$

The extra 1 is for zero

Total numbers required: 2(A + 1)

Remeber min number of bits, *n*, required to represent a decimal number *y* is

n = $\lceil log_2(y) \rceil$

Using y = 2(A + 1)

n = $\lceil log_2(2(A + 1)) \rceil$

= $\lceil log_2(2((6.02 * 10^23) + 1)) \rceil$

Which gives us the value: 80

See the image below for workings. The calculator got 79.994. Rounding it up gives 80. So we need **80 bits** to represent the Avogadro's number.

![Calculation](images/max_bits_for_avogadro-2026-08-06_13-55.png)

### 2.10

1. $invert(1010) + 0001 = 0101 + 0001 = 0110_2$
2. $invert(01011010) + 00000001 = 10100101 + 00000001 = 10100110_2$
3. $invert(11111110) + 00000001 = 00000001 + 00000001 = 00000010_2$
4. $invert(0011 1001 1101 0011) + 0000 0000 0000 0001 = 1100 0110 0010 1100 + 0000 0000 0000 0001 = 1100 0110 0010 1101_2$

### 2.11

For converting negative decimal to 2's complement: convert the magnitude to binary and just add $01_2$ to it.

1. $102_{10} = 2^6 + 2^5 + 2^2 + 2^1 = 0110 0110_2$
2. $64_{10} = 0100 0000_2$
3. $33_{10} = 0010 0001_2$
4. $-128_{10} = 1000 0000_2$
5. $127_{10} = 0111 1111_2$

### 2.12

If the last two digits of a 2's complement binary number are 00, it means the number is a multiple of 4.

### 2.13

Converting 2's complement binary to 8-bit equivalent.

This is sign extension in play. Just repeat the sign bit to fill in the missing bits at the left.

| n-bit | 8-bit |
|:---:|:---:|
| 1010 | 1111 1010 |
| 011001 | 0001 1001 |
| 11 1111 1000 | 1111 1000 |
| 01 | 0000 0001 |

For the third item in the table with 10 bits, just strip off excess bits from the right since they can't be stored.

Alternatively, consider it as unsigned and convert to decimal.

u = 11 1111 1000

y = unsigned_binary_to_decimal(u)

2s_complement_repr_of_u_in_n_bits = y modulo $2^n$


This is also the same as the

= u AND $00 1111 1111_2$

i.e.

= u AND $2^n - 1$

These proposals are from observation

### 2.14

1.
```text
	1011
+	0001
--------
=   1100
```
2.
```text
	0000
+	1010
--------
=   1010
```
3.
```text
	1100
+	0011
--------
=   1111
```
4.
```text
	0101
+	0110
--------
=   1011
```
5. Here the **1** at the 5th position is lost because we are using an implicit 4-bit encoding system
```text
	1111
+	0001
--------
=   0000
```

### 2.15

Shifting a binary number to the right performs division by 2.

### 2.16

Write the results of the following additions as both eight-bit binary and decimal numbers. For each part, use standard binary addition as
described in Section 2.5.1. (+7) + (-7)

For converting negative binary in 2's complement to decimal, invert every single bit and add $01_2$. Get the magnitude and put a negative sign.

#### 1's complement

```text
	0000 0111
+	1111 1000
-------------
2=  1111 1111
10= -0
```

#### Signed magnitude

```text
	0000 0111
+	1000 0111
-------------
2=  1000 1110
10= -14
```

#### 2's complement

There was a discarded carry out of the 8th bit.

```text
	0000 0111
+	1111 1001
-------------
2=  0000 0000
10= 0
```

### 2.17

Add the following 2’s complement binary numbers. Also express the
answer in decimal.

1.
```text
	0001
+	1011
--------
2=	1100
10=	-4
```
2.
```text
	0000 0011
+	0101 0101
-------------
2=	0101 1000
10=	84
```
3.
```text
	0101
+	0110
--------
2=	1011
10=	-5
```
4.
```text
	01
+	10
------
2=	11
10=	-1
```

### 2.18

Add the following unsigned binary numbers. Also, express the answer in
decimal.

1.
```text
	0001
+	1011
--------
2=	1100
10=	12
```

2.
```text
	0000 0011
+	0101 0101
-------------
2=	0101 1000
10=	88
```

3.
```text
	0101
+	0110
--------
2=	1011
10=	11
```

4.
```text
	01
+	10
--------
2=	11
10=	3
```

### 2.19

$-27_10$ as 2's complement

| n-bits | $-27_10$ |
|:---:|:---:|
| 8-bits | 1110 0101 |
| 16-bits |  1111 1111 1110 0101 |
| 32-bits |  1111 1111 1111 1111 1111 1111 1110 0101 |

This illustrates that increasing the number of bits used to represent a 2's complement number is performed repeating the sign bit until you get the required number of bits. This means that Sign extension does not affect the value represented.

### 2.20

1. Decimal: -4 + 3  = -1

Binary
```text
	1100
+	0011
--------
2=	1111
10=	-1
```

2. Decimal: -4 + 4 = 0

Binary
```text
	1100
+	0100
--------
2=	0000
10=	0
```

This generated an overflow but was discarded and resulted in +0 which was the correct answer.

3. Decimal: 7 + 1 = 8

Binary
```text
	0111
+	0001
--------
2=	1000
10=	-8
```

This generated an overflow and gave the next coded number round the clock/range -8 to +7

4. Decimal: -8 - 1 = -9

Binary
```text
	1000
−	0001
--------
2=	0111
10=	+7
```

This generated an underflow since -9 can't be represented as 4-bits 2's complement number.

5. Decimal: +7 + (-7) = 0

Binary
```text
	0111
+	1001
--------
2=	0000
10=	0
```

The addition generated an overflow and resulted in 0 which is the correct answer.
