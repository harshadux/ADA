def linear_search(a,n,x):
    for i in range(0,n):
        if (a[i]==x):
            #return x
            return i
    return -1
#function call
a = [12,8,6,9,14,16,1,3,5]
x = 16
n = len(a)
result = linear_search(a,n,x)
#result = result - 1 
if result != -1:
    print("Value found at index : " , result)
else:
    print("Value not found")