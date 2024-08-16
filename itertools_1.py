from itertools import combinations

S,k=input().split(' ')

k=int(k)
S=''.join(sorted(S))


for i in range(1,k+1):
    new= list(combinations(S,i))
    for i in new:
        print(''.join(i))
        
print("string inserted between values,default a space.")




