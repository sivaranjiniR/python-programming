N,K=[int(x) for x in raw_input().split()]
arr=raw_input()
l = list(map(int,arr.split(' '))) 
i=0
sum=0
while i<K:
	sum=sum+l[i]
	i=i+1
print sum
