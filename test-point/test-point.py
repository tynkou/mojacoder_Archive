n=int(input())
m=list(map(int,input().split()))
l=int(input())
heikin=sum(m)/n
if heikin<=m[l-1]:
  print("Yes")
else:
  print("No")
