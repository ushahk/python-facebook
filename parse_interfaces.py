import re
dt=[]
dtt=[]
ddt={}
dit=[]
drt=[]
drate=[]
with open("show-interfaces.txt") as int:
   sit=int.readlines()

for i in sit:
  if re.match(".*[in,out]put rate [0-9]+ bits/sec.*$",i):
    dt.append(re.match(".*([inout]put) rate ([0-9]+ bits/sec).*$",i))

for i in sit:
  if re.match(".*?[0-9]+\s+is .*?\, line protocol is .*$",i) and not re.match(".*Port-channel[0-9]+\.[0-9]+.*$",i):
    dtt.append(re.match("(.*?[0-9]+)\s+is .*?\, line protocol is .*$",i))

for i in dtt:
  dit.append(i.group(1))

for i in dt:
  drt.append((i.group(1), i.group(2)))

for i in range(0,len(drt),2):
    drate.append(((drt[i][1]).split()[0],(drt[i+1][1]).split()[0]))

data=dict(zip(dit,drate))
for i, v in data.items():
    data[i]=int(v[0])+int(v[1])
rdata={}
for i,v in data.items():
    rdata[v]=i
nrates=sorted(rdata,reverse=1)

print(rdata[nrates[0]])
