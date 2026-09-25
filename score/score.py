N=int(input())
T=list(map(str,input().split()))
Acount=0 #Aの回数をカウント
Bcount=0 #Bの回数をカウント
for x in T:
  if x=="A":
    Acount+=1
  elif x=="B":
    Bcount+=1
if Acount>Bcount:
  print("A")
elif Acount<Bcount:
  print("B")
else:
  print("draw")
