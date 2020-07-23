'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            arr.pop(i)
            count += 1
            i -= 1
        i += 1
    
    for i in range(count):
        arr.append(0)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")