class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1]+[0]*len(digits)


# Exercise II:
# Mar 25, 2023
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = (digits[-1]+1)%10
        flag = (digits[-1]+1)//10
        res = [new]

        for i in reversed(range(len(digits)-1)):
            new = (flag+digits[i])%10
            flag = (flag+digits[i])//10
            res.append(new)

        if flag == 1:
            res.append(1)

        return res[::-1]


# Exercise III:
# Jan 29, 2024
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = (digits[-1]+1)%10
        flag = (digits[-1]+1)//10
        res = [num]

        for i in reversed(range(len(digits)-1)):
            num = (flag+digits[i])%10
            flag = (flag+digits[i])//10
            res.append(num)

        if flag:
            res.append(1)

        return res[::-1]
