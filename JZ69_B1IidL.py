class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1 
        right = len(arr)-2

        while left < right:
            mid = left + (right-left)//2
            print(left, mid, right)
            for item in (left, mid, right):
                print(item, arr[item-1], arr[item], arr[item+1])
                if arr[item] > arr[item-1] and arr[item] > arr[item+1]:
                    return item

            if arr[mid] > arr[mid-1]:
                left = mid 
            elif arr[mid] > arr[mid+1]:
                right = mid 

        return left 
