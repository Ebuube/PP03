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

Proper formula: To represent an alphabet with *n* different characters, the least number of bits required is

$\lceil\log_2(26) \rceil$

