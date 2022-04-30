nums = [1,3,5,6]
target = 5

if (target in nums) == True:
    print(nums.index(target))
else:
    print(0)


# if nums.index(target) > 0:
#     print(nums.index(target))
# else:
#     print(0)

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         result = 0
#         if (target in nums) == True:
#             result = nums.index(target)
#         else:
#             result = 0
#         return result

# class Color:
#     red, green, blue = 0, 0, 0
#
#     def __init__(self, r, g, b):
#         red, green, blue = r, g, b
#
#     def toHex(self):
#         return '#%02x%02x%02x' % (red, green, blue)
#
# class colorAlpha(Color):
#     alpha = 1
#
#     def __int__(self, r, g, b):
#         red, green, blue, aplha = r, g, b, a
#
# gray = Color(80, 80, 80)
#
# red = colorAlpha(255, 0, 0, .5)