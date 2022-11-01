import random
a = []
for _ in range(10):
    a.append(random.randrange(10))

len_of_a=len(a)
print(len_of_a)
a_1half=a[0:len_of_a]
a_1half=a[0:int(len_of_a/2)]
a_2half=a[int(len_of_a/2):len_of_a]
a_1half=sorted(a_1half)
a_2half=sorted(a_2half)
a1=a_1half
b1=a_2half
print(a1)
print(b1)
merged=[]
i=0
j=0
cnt_inv=0
for _ in range(len_of_a):
    if a1[i]<b1[j]:
        # merged.append(a1[i])

        print("(",a1[i],b1[j],')','not inversion')
        i=i+1
        # print(i,"i",j,'j')
    else:
        merged.append((a1[i],b1[j]))
        cnt_inv=cnt_inv+len(a_1half)-i
        # print(cnt_inv)
        print("(",a1[i],b1[j],')','inversion')
        j=j+1
        # print(i,'i',j,'j')
    if i==len(a1):
        break
print(merged)
print(cnt_inv, '= total no of inversions')
