'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


        
    
# # Naive Solution
def find_max(arr):

    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max

def sliding_window_max(nums, k):
    start = 0
    end = k
    result_array_size = len(nums) - (k - 1)
    result = [0] * result_array_size

    for i in range(result_array_size):
        result[i] = find_max(nums[start:end])
        start += 1
        end += 1

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
