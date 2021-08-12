def binary_search(a,left,right,x):
    if right>=left:
            mid = left + right // 2
            if a[mid]==x:
                return x
            elif a[mid] < x:
                return binary_search(a,mid+1,right,x)
            else:
                return binary_search(a,left,mid-1,x)
    else:
           return -1
#function call           
a=[1,2,3,4,5,6,7,8,9]
x = 5
left = 0
right = len(a)-1
result = binary_search(a,left,right,x)
result = result-1
if result != -1:
    print("Value found at index : " , result)
else:
     print("Value not Found")