### 2.41

1. Largest IEEE exponent for 32-bit is stored as 254 which is resolved as +127
2. The smallest IEEE exponent for 32-bit is stored as 1 which is resolved as -126

This is because 0000 0000 is reserved for class zero and 1111 1111 is reserved for class infinity.

### 2.42

A computer programmer wrote a program that adds two numbers. The
programmer ran the program and observed that when 5 is added to 8,
the result is the character m. Explain why this program is behaving
erroneously.

#### Solution

Letter 'm' is the 13th letter in the English alphabet. 5 + 8 = 13. Perhaps he is typecasting the resultant value to character datatype.

### 2.43

 Translate the following ASCII codes into strings of characters by interpreting each group of eight bits as an ASCII character.

1. x48656c6c6f21
=   48	65	6c	6c	6f	21
=   H   e   l   l   o   !
=   Hello!

2. x68454c4c4f21
=   68	45	4c	4c	4f	21	
=   h   E   L   L   O   !
=   heLLO!

3. x436f6d70757465727321
=   43	6f	6d	70	75	74	65	72	73	21	
=   C   o   m   p   u   t   e   r   s   !
=   Computers!

4. x4c432d32
=   4c	43	2d	32	
=   L   C   -   2
=   LC-2

### 2.44

What operation(s) can be used to convert the binary representation for 3 (i.e., 0000 0011) into the ASCII representation for 3 (i.e., 0011 0011)? What about the binary 4 into the ASCII 4? What about any digit?

#### Solution

Just add the binary representation of the number to the ascii representation for '0' (i.e. 0011 0000)

E.g.
$3_{10} = 11_2 = 0000 0011_2$
Add '0' = 0011 0000

3 + '0' = 0000 0011 + 0011 0000 = 0011 0011


### 2.45

Convert the following unsigned binary numbers to hexadecimal.
1. 1101 0001 1010 1111
=   D   1       A   F
= xD1AF

2. 001 1111
=   1   F
= x1F

3. 1
=   1
= x1

4. 1110 1101 1011 0010
=   E   D       B   2
= xEDB2

### 2.46

Convert the following hexadecimal numbers to binary.

1. x10
=   0001 0000
= 00010000

2. x801
=   1000    0000    0001
= 100000000001

3. xF731
=   1111 0111   0011    0001
= 1111011100110001

4. x0F1E2D
=   0000    1111    0001    1110    0010    1101
= 000011110001111000101101

5. xBCAD
=   1011    1100    1010    1101
= 1011110010101101

### 2.47

Convert the following hexadecimal representations of 2’s complement binary numbers to decimal numbers.

1. xF0
=   1111    0000
= 11110000
= -1 * 2^4
= -16

2. x7FF
=   0111    1111    1111
= 011111111111
= 2047

3. x16
=   0001    0110
= 00010110
= 22

4. x8000
= 1000 0000 0000 0000
= 1000000000000000
= $-1 * 2^15$
= -32768

### 2.48

Convert the following decimal numbers to hexadecimal representations of 2’s complement numbers.

1. 256
= +1 * 1 0000 0000
= 0001  0000    0000
= x100

2. 111
= +1 * 0110 1111
= 0110  1111
= x6F

3. 123,456,789
= +1 * 
> Todo: on my own PC

4. −44
= -1 * 0010 1100

invert to get 1101 0011

Then add 1
1101 0100
= xD4

### 2.49

Perform the following additions. The corresponding 16-bit binary numbers are in 2’s complement notation. Provide your answers in hexadecimal.

1.
```text
	x025B
+	x26DE
---------
=	x2939
```

2. Under probation
```text
	x7D96   0111 1101 1001 0110
+	xF0A0   1111 0000 1010 0000
---------   -------------------
=	x6E36  0110 1110 0011 0110
```

3.
```text
	xA397   1010 0011 1001 0111
+	xA35D   1010 0011 0101 1101
---------   -------------------
=	x46F4   0100 0110 1111 0100
```

4.
```text
	x7D96   0111 1101 1001 0110
+	x7412   0111 0100 0001 0010
---------   -------------------
=	xF1A8   1111 0001 1010 1000
```

5. What else can you say about the answers to parts c and d?
In part c,there was an overflow by adding two negative numbers to get a positive number. Where as in part d, there was an overflow by adding two positive numbers to get a negative one.

### 2.50

Perform the following logical operations. Express your answers in hexadecimal notation.

1. x5478 AND xFDEA
```text
    x5478   0101 0100 0111 1000
AND xFDEA   1111 1101 1110 1010
---------   -------------------
=   x5468   0101 0100 0110 1000
```

2. xABCD OR x1234
```text
    xABCD   1010 1011 1100 1101
OR  x1234   0001 0010 0011 0100
---------   -------------------
=   xBBFD   1011 1011 1111 1101
```

3. NOT((NOT(xDEFA)) AND (NOT(xFFFF)))

#### Solution

xDEFA = 1101 1110 1111 1010
NOT(xDEFA) = 0010 0001 0000 0101

xFFFF = 1111 1111 1111 1111
NOT(xFFFF) = 0000 0000 0000 0000


```text
    NOT(xDEFA)  0010 0001 0000 0101
AND NOT(xFFFF)  0000 0000 0000 0000
--------------  -------------------
=   x000        0000 0000 0000 0000
= NOT(x000)
= xFFFF
```

4. x00FF XOR x325C
```text
    x00FF   0000 0000 1111 1111
XOR x325C   0011 0010 0101 1100
---------   -------------------
= x32A3      0011 0010 1010 0011
```
