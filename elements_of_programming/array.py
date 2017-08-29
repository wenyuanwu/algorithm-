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
# A = [0,1,2,0,2,1,1]
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

# A = [{1:"a"}, {1:"b"},{3:"j"}, {2:"c"}, {1:"d"}, {3:"e"}, {2:"f"}, {2:"g"}, {1:"h"}, {3:"i"}]    
# print(same_key(A))

#buy and sell a stock once 

def buy_and_sell_stock_once(A):
    start_idx = 0 
    max = 0 
    while start_idx < len(A) - 1:
        end_idx = start_idx + 1
        print("end_idx", end_idx)
        while end_idx < len(A) and A[end_idx] > A[end_idx - 1]:
            end_idx += 1 
        temp_profit = A[end_idx - 1] - A[start_idx]
        if temp_profit > max:
            max = temp_profit
        start_idx = end_idx
    return max     

# A = [310,315,275,295,260,270,290,230,255,250]
# B = [100,300,250,600,900,10,300]
# print(buy_and_sell_stock_once(A))
# print(buy_and_sell_stock_once(B))

