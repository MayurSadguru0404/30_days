arr = ['flower', 'flow', 'flight']
def longestCommonPrefix(arr):
    if "" in arr or arr == []:
        return ""
    preix = arr[0]
    for i in range(1,len(arr)):
        while(preix != ""):
            try:
                if str.index(str(arr[i]),preix) == 0:
                    break
                else:
                    preix = preix[:-1]
            except:
                
                preix = preix[:-1]
    return preix
 
print("Output 1:",longestCommonPrefix(arr))
print("Output 2:",longestCommonPrefix(arr=["apple", "ape", "april"]))
print("Output 3:",longestCommonPrefix(arr=[""]))
print("Output 4:",longestCommonPrefix(arr=["alone"]))