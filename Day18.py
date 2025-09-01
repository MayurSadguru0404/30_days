def count_divisible(n):
    i = 1
    arr = []
    while i <= n:
        if n % i == 0:
            arr.append(i)
        i += 1 
    return arr

print(count_divisible(12))
