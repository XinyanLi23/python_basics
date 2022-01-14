# sum sub index

#list = range[1:11]

from operator import index


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(nums)

def sub(nums):
    sub_self = [total - x for x in nums ]
    # sub_self = [total - nums[i] for i in range(len(nums))]
    return sub_self

print(sub(nums))

#EX
#[0, 1, 3, 6, ..., 45]
#[54, ... 19, 10, 0]





