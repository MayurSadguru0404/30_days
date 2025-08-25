def generate_permutation(string,start,end):
    current=0
    if (start==end-1):
        print(string)
    else:
        for current in range(start,end):
            x=list(string)
            x[start],x[current]=x[current],x[start]

            generate_permutation("".join(x),start+1,end)
            x[start],x[current]=x[current],x[start]
str="abc"
n=len(str)
generate_permutation(str,0,n)
