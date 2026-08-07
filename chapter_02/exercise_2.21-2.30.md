### 2.21

Scenarios:
1. positive + positive
2. positive + negative
3. negative + negative

> A valid 2's complement number is within range.

Given the numbers *a* and *b*. Overflow occurs if (a + b) > max positive number for n-bits.

Where max positive number for n-bits is $2^{n-1} - 1$.

Underflow is when the sum of addition of (negative numbers especially) result in a negative value too low below the lower range of the n-bit representation.

Where max negative number for n-bits is $2^{n-1}$.

### 2.22

Correct Decimal calulation: 32767 + 1 = 32768
```text
    0111 1111 1111 1111
+   0000 0000 0000 0001
-----------------------
2=  1000 0000 0000 0000
10= -32768
```

This caused an overflow into a negative number.

### 2.23

Overflow occurs in unsigned numbers' addition when the result is greater than $2^n - 1$. Where *n* is the number of bits.

### 2.24

Correct Decimal calulation: Max number possible $2^16 - 1$ = 65535

65535 + 1 = 65536

```text
	1111 1111 1111 1111
+	0000 0000 0000 0001
-----------------------
2=	0000 0000 0000 0000
10=	0
```

This calulation caused an overflow into 0. The extra *1 carry* has to be discarded.

### 2.25

Why does the sum of a negative 2’s complement number and a positive
2’s complement number never generate an overﬂow?

#### Solution

For 2's complement numbers the range is

$-2^{n-1}$ to $+2^{n-1} - 1$.

Where n > 1.

If an overflow is possible, it should be between the largest negative number and the smallest positive number.

Largest negative number (LNN) = $-2^{n-1}$

Smallest positive number (SNN) = +1

LNN + SNN = $-2^{n-1} + 1$

This is within the range: $-2^{n-1}$ to $+2^{n-1} - 1$.

So no overflow is possible when a negative 2's complement number is added to a positive 2's complement number.

### 2.26

You wish to express −64 as a 2’s complement number.

1. How many bits do you need (the minimum number)?

### Solution

Let's say -64 is the minimum negative number = $-(2^{n-1})$

$-64 = -(2^{n-1})$

$64 = 2^{n-1}$

$log_2(64) = n - 1$

$6 = n - 1$

$7 = n$

So you need a minimum of 7-bits to represent -64.

2. With this number of bits, what is the largest positive number you can represent? (Please give answer in both decimal and binary.)

The largest positive number with 7-bits is $2^{n-1} - 1$ ; where n = 7

Which gives +63 as decimal and *011 1111* as binary

3. With this number of bits, what is the largest unsigned number you can represent? (Please give answer in both decimal and binary.)

Largest unsigned number with 7 bits will be $2^n - 1$.

$= 2^7 - 1$

$= 128 - 1 = 127$

127 is hte largest unsigned number representable with 7-bits.

### 2.27

The LC-3, a 16-bit machine, adds the two 2’s complement numbers 0101010101010101 and 0011100111001111, producing 1000111100100100. Is there a problem here? If yes, what is the problem? If no, why not?

```text
	0101010101010101
+	0011100111001111
--------------------
2=	1000111100100100
def=1000111100100100
```

The result from the LC-3 is the correct binary result but it overflowed, resulting in a negative number. The sum of two positive numbers should not be zero.

### 2.28

When is the output of an AND operation equal to 1?

It is only when each operand is 1.

### 2.29

| X | Y | X AND Y |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 2.30

Compute the following. Write your results in binary.

1.
```text
	01010111
AND	11010111
------------
=	01010111
```

2.
```text
	101
AND	110
-------
=	100
```

3.
```text
	11100000
AND	10110100
------------
=	10100000
```

4.
```text
	00011111
AND	10110100
------------
=	00010100
```

5.
```text
	0011
AND	0110
--------
=	0010
AND	1101
--------
=	0000
```

6.
```text
    0110
AND	1101
--------
=	0100
AND 0011
--------
=	0000
```
