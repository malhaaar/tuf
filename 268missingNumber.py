# solution1

n = len(nums)
for i in range(n+1):
    if i in nums:
        pass
    else:
        return i

# solution 2

return sum(range(len(nums)+1)) - sum(nums) #lol
