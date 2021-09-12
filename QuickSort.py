def partition(a,left,right):
    #print(left , right)
    pivot = a[left]
    low = left
    high = right
    while low < high:
        while high >= left and a[high] > pivot :
            high = high -1 
        while low <= right and a[low] <= pivot :
            #print(a[low] ,low )
            low = low + 1
            
        if low < high:
            temp=a[low]
            a[low]=a[high]
            a[high]=temp
    a[left]=a[high]
    a[high]=pivot
    return high

def QuickSort(a,left,right):
    if left<right:
        p = partition(a,left,right)
        #print(p)
        QuickSort(a,left,p-1)
        QuickSort(a,p+1,right)

a = [12,31,45,78,89,45]
left = 0
right = len(a)-1
QuickSort(a,left,right)
print(a)