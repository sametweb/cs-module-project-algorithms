'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    
    # If n is below zero, that means the monster can't eat no more cookies
    # with provided n
    if n < 0:
        return 0

    # If n is 0, that means all cookies are eaten and that counts as one way
    # to eat all cookies
    elif n == 0:
        return 1

    #check if the work has already been done
    #by looking in the cache
    elif cache is not None and cache[n] > 0:

        #return the previously computed answer and don't recurse
        return cache[n]

    # if cache is None or cache[n] is not greater than zero
    else:

        # Might need to create our cache for the first time
        if cache is None:
            cache = [0 for i in range(n+1)]

        #store the value of the recursive call expressions in our cache
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)

    return cache[n]
    


    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6


    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")