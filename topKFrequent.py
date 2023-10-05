class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        hashmap = sorted(hashmap, key=hashmap.get, reverse=True)
        for i in range(k):
            result.append(hashmap[i])

        return result
