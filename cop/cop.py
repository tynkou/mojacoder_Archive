N,O,P=map(int,input().split())
K=int(input())
M=list(map(int,input().split()))
H=list(map(int,input().split()))
ans=0
for x in H:
  if not(x in M):
     ans+=K     
print(ans)
