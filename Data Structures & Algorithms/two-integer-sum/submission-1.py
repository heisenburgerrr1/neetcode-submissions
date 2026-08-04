class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            different = target - nums[i]
            if different in hashmap:
                return [hashmap[different],i]
            hashmap[nums[i]]=i
