nums = [-1, 0, 1, 2, -1, -4]
target = 0

def three_sum(nums, target):
    n = len(nums)
    for i in range(n):
        seen = {}  # Dictionary to store complement and index
        for j in range(i + 1, n):
            complement = target - nums[i] - nums[j]
            if complement in seen:
                print(f"Numbers are: {nums[i]} (index {i}), {nums[j]} (index {j}), {complement} (index {seen[complement]})")
                return [i, j, seen[complement]]
            seen[nums[j]] = j
    print("No three numbers found that add up to the target.")
    return []

# Call the function
result = three_sum(nums, target)
print("Indices:", result)