#  Given two sorted arrays, A and B, where A has a large enough buffer at
#  the end to hold B. Write a method to merge Binto A in sorted order

a=[1,5,8,11,26]
b=[2,13,22,25]

c=a+b

for i in range(len(c)):
    for j in range(len(c)):
        if c[i]<c[j]:
            temp=c[j]
            c[j]=c[i]
            c[i]=temp
print(c)
