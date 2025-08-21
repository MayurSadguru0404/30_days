def trap_rainwater(Arr):
    N = len(Arr)
    left_maximum = N * [0]
    right_maximum = N * [0]
    ans = 0
    for k in range(N):
        if k == 0:
            left_maximum[k] = Arr[k]
            right_maximum[N-1-k] = Arr[N-1-k]
        else:
            left_maximum[k] = max(left_maximum[k-1], Arr[k])
            right_maximum[N-1-k] = max(right_maximum[N-k], Arr[N-1-k])
    for k in range(N):
        ans += (min(left_maximum[k], right_maximum[k]) - Arr[k])
    return ans

print(trap_rainwater(Arr=[0,1,0,2,1,0,1,3,2,1,2,1]))