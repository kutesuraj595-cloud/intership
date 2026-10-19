def total(*nums):
    s = 0
    for n in nums:
         s += n
    return s
print(total(1,2,3,4,5))