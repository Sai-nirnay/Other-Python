'''You are given n disks placed on a starting rod (from), with the smallest disk on top and the largest at the bottom. There are three rods: the starting rod(from), the target rod (to), and an auxiliary rod (aux).
You have to calculate the minimum number of moves required to transfer all n disks from the starting rod to the target rod, following these rules:
      1. Only one disk can be moved at a time.
      2. A disk can only be placed on top of a larger disk or on an empty rod.
Return the minimum number of moves needed to complete the task.
'''


def  towerOfHanoi(n, fromm, to, aux):
        if n == 0:
            return 0
            
        # Step 1: Move n-1 disks from 'fromm' to 'aux' using 'to'
        moves = towerOfHanoi(n - 1, fromm, aux, to)
        
        # Step 2: Move the nth disk from 'fromm' to 'to'
        # (Optional: If the problem requires printing the steps, you've done 1 actual move here)
        moves += 1 
        
        # Step 3: Move the n-1 disks from 'aux' to 'to' using 'fromm'
        moves += towerOfHanoi(n - 1, aux, to, fromm)
        
        return moves

n = int(input("Enter the number of disks: "))
print("Minimum number of moves required:", towerOfHanoi(n, 'A', 'C', 'B'))