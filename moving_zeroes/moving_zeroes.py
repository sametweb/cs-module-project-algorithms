'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    #initialize a left and right pointer
    #left is 0
    #right is last index in arr
    left = 0
    right = len(arr) - 1

    # use a while loop while left <= right:
    while left < right:

        # if left points at a zero and right points at non-zero
        # swap left and right items in original array
        # increment left
        # decrement right
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        # else
        else:
            # if left is non-zero:
            if arr[left] != 0:
                left += 1
                # increment left
            # if right is zero:
            if arr[right] == 0:
                right -= 1
                # decrement right

    return arr

    # #My first solution
    # count = 0
    # i = 0
    # while i < len(arr) - 1: # O(n^2)
    #     if arr[i] == 0:
    #         arr.pop(i) # O(n)
    #         count += 1
    #         i -= 1
    #     i += 1
    
    # for i in range(count):
    #     arr.append(0)

    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2, 4, 7, 8, 0, 0, 0, 0, 4, 67, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")