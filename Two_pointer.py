# two pointer technique
# def two_pointers_algorithm(array):
#     left = 0
#     right = len(array) - 1
    
#     while left < right:
#         # Perform some operation involving array[left] and array[right]
#         if condition_met:
#             # Adjust pointers as needed
#             left += 1
#             right -= 1
#         elif some_other_condition:
#             left += 1
#         else:
#             right -= 1

            
# example of two sum array
def two_sum_array(nums, target):
    left, right = 0, len(nums)-1
    
    while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return []
           