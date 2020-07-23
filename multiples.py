# Plan

# Iterate length times starting from 1 to length
# In each iteration, multiply the num with the iteration count
# Create a new list with results
# List comprehension looks like a good idea

def list_of_multiples(num, length):
    return [i * num for i in range(1, length + 1)]