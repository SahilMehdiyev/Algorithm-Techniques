
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
