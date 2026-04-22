import array

nums = array.array("i")

nums.append(34)
nums.append(12)
nums.append(22)
nums.append(54)

print(f"First value: {nums[0]}")
print(nums)

# nums.append("five")
# print(f"Last value: {nums[len(nums)-1]}")

print(f"Third value: {nums[2]}")
print(f"Second value: {nums[1]}")
print(f"First value: {nums[0]}")
print(f"Last value: {nums[-1]}")

nums.append("six")