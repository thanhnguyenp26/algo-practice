# def moveZeroes(nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
        
#         l = 0
#         for r in range(len(nums)):
#             if nums[r]:
#                 nums[r], nums[l] = nums[l], nums[r]
#                 l += 1
#         return nums

# print(moveZeroes([0 ,1, 1 ,3 ,12]))         

def lengthOfLongestSubstring(s):
        max_res = 0
        i = 0
        while i < len(s):
            pos = {}
            pos[s[i]] = i
            res = 1
            
            if max_res < res:
                max_res = res
            
            j = i + 1
            if j == len(s):
                return max_res
            while j < len(s):
                if s[j] in pos:
                    i = pos[s[j]]
                    break
                else:
                    pos[s[j]] = j
                    res += 1
                    if max_res < res:
                        max_res = res
                    j += 1
            i += 1
        return max_res
print(lengthOfLongestSubstring('ab'))         
