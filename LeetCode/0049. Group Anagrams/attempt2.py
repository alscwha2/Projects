from collections import defaultdict as defaultdict

'''
	This is the more intuitive way to do it.
	But this should be slower for longer strings because sorting is NlogN
'''

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		map = defaultdict(list)

		for s in strs:
			map[tuple(sorted(s))].append(s)

		return [map[k] for k in map]