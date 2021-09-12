def insertionsort(a,n):
    for j in range(2,n):
        key=a[j]
        i = j-1
        while(j>0 and a[j]>key):
            a[j+1]=a[j]
            j = j-1
            a[j+1]=key 
a=[12,15,4,8,93,5]
insertionsort(a,len(a)-1)
print(a)