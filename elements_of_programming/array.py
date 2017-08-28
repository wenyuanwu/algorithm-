# the dutch national flag problem

def partition(A, i):
    val = A[i]
    # left, right = 0, len(A) - 1
    smaller = 0 
    for j in range(len(A)):
        if A[j] < val: 
            A[smaller], A[j] = A[j], A[smaller]
            smaller += 1
    
    larger = len(A) - 1
    for h in reversed(range(len(A))):
        if h < smaller:
            break
        elif A[h] > val:
            A[h], A[larger] = A[larger], A[h]
            larger -= 1
    return A 

# test case
A = [0,1,2,0,2,1,1]

# print (partition(A,3), "result1") 
# [0,0,1,2,2,1,1]
# print (partition(A,2), "result2") 
# [0,1,0,1,1,2,2]

