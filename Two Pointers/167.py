def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1
    while end > start:
        if numbers[start] + numbers[end] < target:
            start += 1
        elif numbers[start] + numbers[end] > target:
            end -= 1
        else:
            return [start+1, end+1]

numbers = [-1,0]
target = -1
result = twoSum(numbers, target)
print(result)