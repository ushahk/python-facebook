def scnd_val(lis):
  d=dict(lis)
  sv=sorted(d.values())
  plh=0
  v=[]
  p=sv[0]
  for i in range(1,len(sv)):
    if sv[0]!=sv[i] and plh==0:
      p=sv[i]
      plh=1
      v.append(i)
    elif p!=sv[i] and plh==1:
      break
    elif p==sv[i] and plh==1:
      v.append(i)
  values=[]
  for i in v: values.append(sv[i])
  names=[]
  for i,j in d.items():
    if j==values[0]:
      names.append(i)
  return sorted(names)

lis=[]
li=input().split()
li.pop(0)
for i in range(0,len(li),2): lis.append(li[i:i+2])
scnd_val(lis)
