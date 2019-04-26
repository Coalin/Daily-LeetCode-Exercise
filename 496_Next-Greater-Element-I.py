# Method I:
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for num in nums1:
            index = 0
            cur_num_index = 0
            
            while index <= len(nums2)-1:
                if nums2[index] == num:
                    cur_num_index = index
                    break
                else:
                    index += 1
            
            # print(cur_num_index)
            
            while cur_num_index <= len(nums2)-1:
                if nums2[cur_num_index] > num:
                    res.append(nums2[cur_num_index])
                    break
                elif cur_num_index == len(nums2)-1:
                    res.append(-1)
                    break
                else:
                    cur_num_index += 1
                    
            # print(res)
        
        return res
        
 
# Method II:
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        
        res = []
        my_stack = []
        my_dict = {}
        
        my_stack.append(nums2[0])
        
        for num in nums2[1:]:
            while my_stack:
                if num > my_stack[-1]:
                    my_dict[my_stack.pop()] = num
                else:
                    break
            my_stack.append(num)
            
        for key in my_stack:
            my_dict[key] = -1
            
        for i in nums1:
            res.append(my_dict[i])
            
        return res        
