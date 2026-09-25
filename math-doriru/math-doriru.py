N=int(input())
for i in range(N):
  A,B,K=map(int,input().split())
  if A+B==K:
    print("Yes")
  else:
    print("No")
