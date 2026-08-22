### 3.1

Gate = 1: N-type is closed and P-type is open
Gate = 0: N-type is open and P-type is closed

### 3.2 

See in ![Circuit_3.2](images/circuit_3.2.png)

### 3.3

AND, OR, NAND, NOR, XOR

There are five of them.

### 3.4

See in ![Circuit_3.4](images/circuit_3.4.png)

Truth table of the circuit

| A | B | C |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

This is typical of a NOR gate

### 3.5

| A | B | C | OUT |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 |

This looks like a table for

OUT = NOT(C) AND (NOT(A) OR NOT(B))

### 3.6

| A | B ||  C | D | Z |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | | 1 | 1 | 0 |
| 0 | 1 | | 1 | 0 | 0 |
| 1 | 0 | | 0 | 1 | 0 |
| 1 | 1 | | 0 | 0 | 1 |

This is a truth table for AND gate

Z = C NOR D

C = NOT A

D = NOT B

### 3.7

In volts.

| A | B | OUT |
|:---:|:---:|:---:|
| 0 | 0 | 5 |
| 0 | 5 | 2.5 |
| 5 | 0 | 2.5 |
| 5 | 5 | 0 |

So when A is different from B, the output is indeterminate. Since it is not specifically high or low logic output but in betweeen. This could be because of short circuting that grounds the inputs from the p-type transistors.

### 3.8

See in ![Circuit.3.8](images/circuit_3.8.png)

### 3.9

The circuit links the output of one inverter into another inverter.

OUT = NOT(NOT(A))

### 3.10

1 = NOT(A) AND NOT(B) AND C AND D AND E AND NOT(F)
