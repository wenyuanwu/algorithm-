# the dutch national flag problem

def partition(A, i):
    val = A[i]
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

# -------------------------------------------
# variant
# all objects w/ same key appear together 

def same_key(A):
    pointer_1, pointer_2, pointer_3 = 0, 0, len(A)
    while pointer_2 < pointer_3:
        k, v = list(A[pointer_2].items())[0]
        if k == 1: 
            A[pointer_1], A[pointer_2] = A[pointer_2], A[pointer_1]
            pointer_1 += 1
            pointer_2 += 1 
        elif k == 2:
            pointer_2 += 1
        else: 
            pointer_3 -= 1 
            A[pointer_2], A[pointer_3] = A[pointer_3], A[pointer_2]
    return A 

A = [{1:"a"}, {1:"b"}, {2:"c"}, {1:"d"}, {3:"e"}, {2:"f"}, {2:"g"}, {1:"h"}]    
print(same_key(A))

