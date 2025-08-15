t=[0,1,2,1,0,2,1,0]
high,low,mid=-1,0,0
while True:
    if(len(t)+high)==(mid-1):
        break
    if t[mid]==2:
        t[mid]=t[high]
        t[high]=2
        high-=1
    elif t[mid]==0:
        t[mid]=t[low]
        t[low]=0
        mid+=1
        low+=1
    elif t[mid]==1:
        mid+=1
print(t)