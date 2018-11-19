import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = ""
        num_dic = {}
        for item in nums:
            str_item = str(item)
            number = int(str_item[0])
            if number in num_dic:
                num_dic[number].append(str_item)
            else:
                num_dic[number] = []
                num_dic[number].append(str_item)
        for index in num_dic:
            num_dic[index] = sorted(num_dic[index], reverse = True, key=functools.cmp_to_key(self.compare))
        for i in reversed(range(10)):
            if i in num_dic:
                for j in num_dic[i]:
                    res += str(j)
        return str(int(res))
    
    def compare(self, str_num1, str_num2):
        num1 = int(str_num1 + str_num2)
        num2 = int(str_num2 + str_num1)
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        else:
            return 0
        
        
