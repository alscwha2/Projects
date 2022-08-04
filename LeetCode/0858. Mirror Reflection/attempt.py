from typing import List
from sys import argv as argv
'''
* Taking the bottom left corner as the origin (0,0), the laser is going to end up in either (0,p) (p,0) or (p,p). 
* Every time the laser hits an EAST/WEST wall, it has moved by q.

	If p = odd, q = even: return 0.

* Therefore, if q is even and p is odd, how can the laser possibly end up in the vertical p position? It starts at zero and moves upwards by an even number every time, so it can't end up in an odd position! Therefore, the y coordinate when q is even and p is odd must be Zero. Hence, If p = odd, q = even: return 0.

	If p = even, q = odd: return 2

* Remember that the laser is starting at Zero and moving up by q every time. Let's say q is odd and p is even. In order to make an odd number even, you have to multiply it by an even number. What that means here is that the laser will have to travel an even number of times in order to get into a corner. If it starts on the WEST and traverses the EAST/WEST gap an even number of times, that means that it must end up back where it started - on the WEST. The only corner on the WEST is number 2; the alternative would be it ending up at its starting point and we would have an infinite loop - it will never reach a corner.

	If p = odd, q = odd: return 1

* Let's say it traverses an odd amount of times before hitting the corner. If so, it would end on the EAST. And it must also end on the NORTH because since it traversed an odd amount of times and q is odd therefore its y position moved by an odd amount, and for it to end up on the south it would have to move an even amount. Therefore, if it travels an odd amount of times, it ends up in #1.
* Let's say it traverses an even amount of times. That means that it's going to end up on the WEST wall, and it's y position must be even as well. But since the y position can only be Zero or p, and p is odd, therefore its y position must be Zero. Meaning it would end up back in the origin (0,0), and we have an infinite loop - it will never end up in a corner. Therefore, this isn't an option. It must have traveled an odd amount of times and ended up in #2.
'''

class Solution:
	def mirrorReflection(self, p: int, q: int) -> int:
		while p % 2 == 0 and q % 2 == 0:
			p, q = p // 2, q // 2
		return 1 - p % 2 + q % 2


# argv[1]
# print(Solution().mirrorReflection(24,36))