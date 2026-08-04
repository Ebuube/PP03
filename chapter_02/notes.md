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

0-01111011-00000000000000000000000

Normalized form says

-1<sup>S</sup> * 1.fraction * 2<sup>exponent - 127</sup>, 1 <= exponent <= 254

For the number *a*:

S = 0 i.e. positive sign

exponent field = 01111011<sub>2</sub> = 123<sub>10</sub>

fraction field = 00000000000000000000000<sub>2</sub> = 0<sub>10</sub>

Therefore:
*a*<sub>10</sub> = -1<sup>0</sup> * 1.0 * 2<sup>123 - 127</sup>

= 1 * 1.0 * 2<sup>-4</sup>
*a*<sub>10</sub>= 0.0625
