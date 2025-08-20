def zer_subarray(arr):
    sum=0
    h_map={0:[-1]}
    result=[]

    for i,num in enumerate(arr):
        sum +=num

        if sum in h_map:
            for start in h_map[sum]:
                result.append((start+1,i))
        h_map.setdefault(sum,[]).append(i)
    return result

print(zer_subarray([1,2,-3,3,-1,2]))
print(zer_subarray([4,-1,-3,1,2,-1]))
print(zer_subarray([1,2,3,4]))
print(zer_subarray([0,0,0]))