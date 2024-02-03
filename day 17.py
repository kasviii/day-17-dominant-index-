def dominant_index(nums):
   """
   Determines whether the largest element in the array is at least twice as much as every other number in the array.
   If it is, returns the index of the largest element, or returns -1 otherwise.

   Args:
       nums: The input array of numbers.

   Returns:
       The index of the largest element if it's twice as much as every other number, -1 otherwise.
   """

   if not nums:  # Handle empty arrays
       return -1

   max_index = 0
   max_value = nums[0]

   for i in range(1, len(nums)):
       if nums[i] > max_value:
           max_index = i
           max_value = nums[i]

   # Check if the largest element is at least twice as much as every other number
   for i in range(len(nums)):
       if i != max_index and max_value < 2 * nums[i]:
           return -1

   return max_index

# Get input from the user
nums = input("Enter the array elements separated by spaces: ").split()
nums = [int(num) for num in nums]  # Convert strings to integers

# Call the function and print the result
result = dominant_index(nums)
print("The index of the dominant element is:", result)
