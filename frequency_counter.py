nums = [1,2,2,2,3,4,4]
freq = {}

for i in nums:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print(freq)