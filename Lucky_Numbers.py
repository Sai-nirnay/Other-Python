'''A lucky number is defined using a special elimination process:
   1. Start with natural numbers: 1, 2, 3, 4, 5, 6, ...
   2. In the 1st step, remove every 2nd number.
   3. In the 2nd step, remove every 3rd remaining number.
   4. In the 3rd step, remove every 4th remaining number, and so on...
This continues indefinitely. Given an integer n, determine if it remains after all steps.
Return 1 if n is a lucky number, otherwise return 0.
'''

def isLucky(n): 
    # Start by tracking the number's initial position
    position = n
    counter = 2
    
    # Loop continues as long as the deletion step can reach our number's position
    while counter <= position:
        # If the position is perfectly divisible by the counter, it gets eliminated
        if position % counter == 0:
            return 0  # Not a lucky number
            
        # Update the position by subtracting the number of elements removed before it
        position -= position // counter
        
        # Move to the next elimination round (e.g., from 2nd to 3rd, then 4th...)
        counter += 1
        
    return 1  # The number survived all rounds, it is a lucky number

# Driver code to test the function
n = int(input("Enter a number to check if it is lucky or not: "))
print(isLucky(n))