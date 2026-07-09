#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # self.quick_sort(nums, 0, len(nums)-1)
        nums = self.merge_sort(nums)


        return nums

    def quick_sort(self, nums: List[int], left: int, right: int):
        
        if left >= right:
            return 
            
        
        # pivot_idx = self.partition(nums, left, right)

        # left recursive
        # self.quick_sort(nums, left, pivot_idx-1)
        # # right recusive
        # self.quick_sort(nums, pivot_idx+1, right)

        lt, gt = self.partition3(nums, left, right)

        # left recursive
        self.quick_sort(nums, left, lt-1)
        # right recusive
        self.quick_sort(nums, gt+1, right)


    # def partition(self, nums: List[int], left:int, right:int):
    #     """
    #     two ways quick sort
    #     """

    #     # selt random index as pivot index 
    #     rand_idx = random.randint(left, right)
    #     # storage at right idx
    #     nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
    #     pivot_val = nums[right]

    #     i = left
    #     for j in range(left, right):

    #         # the value small then pivot been move to front
    #         if nums[j] < pivot_val:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1  # point to next positon of samll boundary

    #     nums[i], nums[right] = nums[right], nums[i]

    #     return i # pivot_idx = i
    

    def partition3(self, nums: List[int], left:int, right:int):
        """
        three-way quick sort
        """
        # selt random index as pivot index 
        rand_idx = random.randint(left, right)
        # storage at right idx
        nums[rand_idx], nums[left] = nums[left], nums[rand_idx]
        pivot_val = nums[left]

        lt = left
        gt = right
        i = left+1 # scan point

        while i <= gt:
            if nums[i] < pivot_val:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > pivot_val:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else: # val== pivot
                i += 1

        return lt, gt    


    def merge_sort(self, arr: List[int]) :
        if len(arr) <= 1:
            return arr 

        mid = len(arr) // 2
        # left recursive
        left = self.merge_sort(arr[:mid]) 
        # right recursive
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)
    

    def merge(self, left, right):
        """
        sort and merge tow list
        """
        res = []
        i = 0  # left point
        j = 0 # right point
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])

        return res
          
# @lc code=end

