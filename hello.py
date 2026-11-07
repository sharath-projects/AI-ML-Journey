A=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    elem=int(input("Enter element: "))
    A.append(elem)
print( A)
sum=0
for j in A:
    sum+=j
mean=sum/n
print("Mean of the elements is:", mean)
vard=0
for k in A:
    vard+=(k-mean)**2
variance=vard/n
print(f"variance ={variance}")
print(f"std dev={variance**0.5}")