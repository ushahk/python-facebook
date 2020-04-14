def ditcs(b):
  db={}
  for i in b: db[i]=None
  for i,j in enumerate(b):
    if db[j] is None:
      db[j]=str(i)
    else:
      db[j]=db[j]+str(i)
  return db

def sol(a,b):
  da=ditcs(a)
  db=ditcs(b)
  for i in da.values():
    iso=''
    if i in db.values():
      iso=True
      continue
    else:
      iso=False
      break
  print(iso)

  sol(a,b)
