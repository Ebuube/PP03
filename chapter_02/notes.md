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

### 1st DeMorgan's Law: ~(~A AND ~B) = A OR B

| A | B | ~A | ~B | ~(~A AND ~B) | A OR B |
|:-:|:-:|:--:|:--:|:------------:|:------:|
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 |
