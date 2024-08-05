class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=(nums)
        x=set()
        for i in nums:
            if i in x: x.remove(i)
            else: x.add(i)
        return (list(x)[0])