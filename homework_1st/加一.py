class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l-1
        while i >= 0:
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0: # 如果末位不是9（不需要进位），则直接返回
                return digits
            i -= 1
        digits.insert(0,1) # 如果原列表每一位都进位了，没有执行上面的return，则最前面添加一位1
        return digits

## 地址：https://leetcode-cn.com/problems/plus-one/