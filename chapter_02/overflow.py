#!/usr/bin/env python3

def is_overflow_2s_complement(n, m, s):
    """
    Check if the sum, s, of n and m is an overflow or not in an 4-bit 2's complement binary system

    Return 1000 if yes overflow, else 0000
    """
    ans = ((~(n ^ m)) & (n ^ s)) & 0b1000

    return bin(ans)
