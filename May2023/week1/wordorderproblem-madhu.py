# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
k=[]
for i in range(n):
    k.append(input())

output=[]
counts=[]

dict={}
for i in k:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

print(len(dict.keys()))
print(*dict.values())
