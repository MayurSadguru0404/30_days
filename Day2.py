def find_missing_num(arr):
    n=len(arr)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    missing_num=expected_sum-actual_sum
    return missing_num

#example
array1=[1,3,4,5]
missing=find_missing_num(array1)
print(f"Missing Number :{missing}")