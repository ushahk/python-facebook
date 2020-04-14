def isHappy(a):
    h=0
    h=loop_more(a)
    while h!=1:
        h=loop_more(h)
    if h==1:
        return True

def loop_more(x):
    x=str(x)
    k=0
    for i in x:
        k+=int(i)**2
    return k
isHappy(input())
