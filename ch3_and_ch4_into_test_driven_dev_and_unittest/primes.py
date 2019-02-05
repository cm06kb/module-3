#----------------------------CHAPTER 4--------------------------------

#-------------------------------------TASK 1------------------

def is_prime(number):
    """
        return true if *number* is prime
    """
    for element in range(2, number):
        if number  % element ==0:
            return false
    return True

def print_next_prime(number):
    """
        print the closest prime number larger than *number*
        
    """
    
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)