from math import log2

"""
    You can use bitwise as well, but that is dependant on the integer encoding

    There was a very interesting approach as well, saying that if you do bitwise
        AND between a power of 2 and the next lowest number it will always equal 
        0, and if it is not a power of 2 it will never equal zero. I have to think
        about that more.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log2(n) % 1 == 0
