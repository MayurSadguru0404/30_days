arr1=[1,3,5]
arr2=[2,4,6]

merged_arr=arr1+arr2
for i in range(len(merged_arr)):
    for j in range(i+1,len(merged_arr)):
        if merged_arr[i]>merged_arr[j]:
            merged_arr[i],merged_arr[j]=merged_arr[j],merged_arr[i]
arr1=merged_arr[0:len(merged_arr)//2]
arr2=merged_arr[(len(merged_arr)//2):len(merged_arr)]
print(f"arr1={arr1}\narr2={arr2}")

