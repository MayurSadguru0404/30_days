def LeaderinArray(arr, n):
    leaders=[]
    for i in range(0,n):
        k = arr[i]         
        isBreak=0
        for j in range(i+1,n):
            if(arr[j]>=k):   
                isBreak=1
                break        
        if(isBreak==0):
            leaders.append(k)
    print(f"Leaders:{leaders}")
              

arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
LeaderinArray(arr, n)