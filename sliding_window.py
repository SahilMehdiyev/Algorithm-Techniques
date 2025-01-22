import random
import time
# ------------- brute_force_solution -------------

def brute_force_solution(arr,k):
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n - k + 1):
        curren_sum = 0
        for j in range(k):
            curren_sum += arr[i + j]

        max_sum = max(curren_sum, max_sum)

    return max_sum


arr = [1,4,2,10,2,3,1,0,20]
k = 4
print(brute_force_solution(arr,k))  # Output: 24

# ------------- sliding_window -------------

def sliding_window_solution(arr,k):
    n = len(arr)

    window_sum = sum(arr[:k])
    max_num = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_num, window_sum)

    return max_sum

print(sliding_window_solution(arr,k))


new_arr = [random.randint(1,1000) for _ in range(1000000)]
k = 50

start_time = time.time()
sliding_window_solution(new_arr,k)
sliding_window_duration = time.time() - start_time

start_time = time.time()
brute_force_solution(new_arr,k)
brute_force_duration = time.time() - start_time

print(f'Sliding window solution: {sliding_window_solution:.6f} sec')
print(f'Brute force solution: {brute_force_solution:.6f} sec')