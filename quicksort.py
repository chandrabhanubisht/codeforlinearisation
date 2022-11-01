import random
a = [9,8,56,6,11,4,3,17,1,7]

# for _ in range(10):
#     a.append(random.randrange(10))
def quicksort(a):
    pivot=a[0]
    print(pivot,' is pivot')
    upper=[]
    lower=[]
    for i in a:
        if i < pivot:
            lower.append(i)
        elif i>=pivot:
            upper.append(i)

    a = []
    x=lower
    y=upper
    for i in lower:
        a.append(i)

    for j in upper:
        a.append(j)
    print(lower,'is lower')
    print(upper,'is upper')
    print(a,'is main array')

    print(a,"a value next")
    # x=[]

    if len(lower)==0:
        return a
    else :
        quicksort(a)



quicksort(a)

