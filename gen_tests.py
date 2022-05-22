import random
import statistics

for i in range(13):

    size = random.randint(0, 19)

    nums = []
    for a in range(size):
        nums.append(random.randint(-10, 80))
    
    rev = []
    for i in reversed(nums):
        rev.append(i)
    
    print(f"    (({nums},), {rev}),")
