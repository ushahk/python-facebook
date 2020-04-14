def num_prime(x):
  nums=[]
  c=0
  for i in range(1,x):
    #print("i={}".format(i))
    p=0
    if i!=2:
      for j in range(2,i):
        #print("j={}".format(j))
        if i%j!=0:
          p=1
          #print("p={}".format(p))
          continue
        elif i%j==0:
          p=0
          #print("p={}".format(p))
          break
    else:
      p=1
    if p==1:
      c+=1
      nums.append(i)
  return (c,nums)
