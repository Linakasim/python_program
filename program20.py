l=[]
n=int(input("enter a limit:"))
for i in range(n):
    v=int(input("Enter values:"))
    l.append(v)
print(l)
c=[n for x in l if x%2!=0]
print("list of non even numbers",c)
