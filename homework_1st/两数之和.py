# 暴力解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

# 优化
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(1,lens):
            another = target-nums[i]
            temp = nums[:i]
            if (target-nums[i]) in temp:
                return [temp.index(target-nums[i]),i]

# hash表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(0,lens):
            another = target-nums[i]
            temp = nums[i+1:]
            if (target-nums[i]) in temp:
                return [i,temp.index(target-nums[i])+i+1]
# hash表优化
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,element in enumerate(nums):
            if hashmap.get(target-element) is not None:
                return [index,hashmap.get(target-element)]
            hashmap[element] = index

## 地址：https://leetcode-cn.com/problems/two-sum/