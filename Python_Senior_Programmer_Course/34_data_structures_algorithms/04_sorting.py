def bubble_sort(values):
    a=values[:]
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]: a[j],a[j+1]=a[j+1],a[j]
    return a
print(bubble_sort([5,2,4,1,3]))