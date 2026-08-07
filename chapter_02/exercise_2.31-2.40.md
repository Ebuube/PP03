### 2.31

The output of an OR operation is equal to 1 if any of the operands is 1.

### 2.32

| X | Y | X OR Y |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### 2.33

1.
```text
    01010111
OR  11010111
------------
=	11010111
```

2.
```text
    101
OR  110
-------
=	111
```

3.
```text
    11100000
OR  10110100
------------
=	11110100
```

4.
```text
    00011111
OR  10110100
------------
=	10111111
```

5.
```text
    0101
OR  1100
--------
=	1101
OR  1101
--------
=	1101
```

6.
```text
    1100
OR  1101
--------
=	1101
OR  0101
--------
=	1101
```

### 2.34

1. NOT(1011) OR NOT(1100)

= 0100 OR 0011

= 0111

2. NOT(1000 AND (1100 OR 0101))

= NOT(1000 AND 1101)

= NOT(1000)

= 0111

3. NOT(NOT(1101))

= NOT(0010)

= 1101

4. (0110 OR 0000) AND 1111

= 01110 AND 1111

= 1111

### 2.35

Masks are used to retrieve/set bits at certain positions in a bit vector.

### 2.36

Busyness bit vector 0110 0010.

- Use a logical AND to set a bit vector as 0.
- Use a logical OR to set a bit vector as 1

1. 1111 1011 with an AND operator
2. 0100 0100 with an OR operator
3. 0000 0000 with an AND operator
4. 11111111 with an OR operator
5. Retrieving status bit of machine 2 as a sign bit.

#### Solution

bit 2 is five positions away from the leftmost bit. Leftward shift of the bit vector 5 times will get the 2nd bit to the 7th position. We can use a bit mask of the 1000 0000 and operator AND to to annul the other bits.

status of bit 2 = (BUSYNESS vector << 5) AND 1000 0000

In general for the BUSYNESS vector with n-bits, to isolate the status of bit of machine *x*,

$status(x^th) = (BUSYNESS << (n-x)) AND 2^n$

Alternatively, you may add the bit pattern to itself. And the result to itself again, and again. Doing so in an n-bit vector for (n - x - 1) number of times will isolate the $x^th$

### 2.37

If n and m are both four-bit 2’s complement numbers, and s is the four-bit result of adding them together, how can we determine, using only the logical operations described in Section 2.6, if an overﬂow occurred during the addition? Develop a “procedure” for doing so. The inputs to the procedure are n, m, and s, and the output will be a bit pattern of all 0s (0000) if no overﬂow occurred and 1000 if an overﬂow did occur.

#### Solution

Criteria for Addition operation with no overflow.

- if sign bit of both operands is 1, then the result should have a sign bit of 1.
- if sign bit of both operands is 0, then the result should have a sign bit of 0.
- if sign bit of both operands are different, an overflow is not possible. So ignore.

This means that an overflow occurs if sign bit of n and m are the same but not the same with the sign bit of the result.

Steps:

1. Perform AND operation on both *n* and *m*.
2. Perform XOR operation with the result from step 1 and *s*.
3. Use sign-bit mask 1000 perform AND operation with the result from step 2.

Summary of function *is_overflow*.

is_overflow(n, m, s) = ((n AND m) XOR s) AND 1000

Returns 0000 if no overflow.

Returns 1000 if yes overflow.

> **XOR** means Is truly different

### 2.38

If n and m are both four-bit unsigned numbers, and s is the four-bit result of adding them together, how can we determine, using only the logical operations described in Section 2.6, if an overﬂow occurred during the addition? Develop a “procedure” for doing so. The inputs to the procedure are n, m, and s, and the output will be a bit pattern of all 0s (0000) if no overﬂow occurred and 1000 if an overﬂow did occur.

#### Solution

For unsigned numbers *n* and *m* being added to get *s*,
Let $n_3, m_3, s_3$ be the leftmost bits.

An overflow occurs if $n_3$ or $m_3$ is 1 and $s_3$ is not 1.
An overflow also occurs if both $n_3$ and $m_3$ are 1.

$is_overflow(n, m, s) = (n_3 AND m_3) OR ((n_3 OR m_3) AND (NOT s_3))$

Returns 0000 if no overflow.

Returns 1000 if yes overflow.

### 2.39

Write IEEE ﬂoating point representation of the following
decimal numbers.

1. 0 10000000 11100000000000000000000
2. 1 10000100 10111010111000000000000
3. 0 00000000 00000000000000000000000
4. 0 10001110 11110100000000000000000

# Rough work
