# sliding window

def maxSum(arr, k):
	# length of the array
	n = len(arr)

	# length of array must be greater
        # window size
	if n < k:
		# print("Invalid")
		return -1

	# sum of first k elements
	window_sum = sum(arr[:k])
	max_sum = window_sum

	# remove the  first element of previous
	# window and add the last element of
	# the current window to calculate the 
    # the sums of remaining windows by
	for i in range(n - k):
		window_sum = window_sum - arr[i] + arr[i + k]
		max_sum = max(window_sum, max_sum)

	return max_sum

arr = [16, 12, 9, 19, 11, 8]
k = 3
print(maxSum(arr, k))


    
   