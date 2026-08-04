class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            print(f"l:{l},r:{r}")
            curSUM = numbers[l] + numbers[r]
            
            if curSUM > target:
                r -= 1
            elif curSUM < target:
                l += 1
            else: 
                return [l+1, r+1]
        return []



