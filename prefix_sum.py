import random
import time
import tracemalloc

def brute_force_solution(arr,queries):
    result = []
    for i, r in queries:
        total = 0
        for i in range(i - 1, r):
            total += arr[i]
        result.append(total)
    return result

arr = [3,6,2,8,9,2]
queries = [(2,5),(4,6),(1,5),(3,6)]
print('Brute force results: ',brute_force_solution(arr,queries))


        