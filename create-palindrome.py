def palindrome_center(c):
    p={}
    q={}
    for i in range (1,len(c)):
        for j in range(1,len(c)):
            if i-j>-1 and i+j<len(c) and c[i-j]==c[i+j]:
                p[i]=j
            else:
                break
    for i in range (1,int(len(c)/2)+1):
        for j in range(1,int(len(c)/2),1):
            if i-j>-1 and i+j<len(c) and c[i]==c[i-1]:
                q[i]=j
            else:
                break
    if p:
        pv=list(p.values())[0]
        return len(c)-pv+1-(pv+2)
    elif q:
        qv=list(q.values())[0]
        return len(c)-qv+1-(qv+1)
    else:
        return len(c)

def create_palindrome(x):
    mark=palindrome_center(x)
    for i in range(mark,0,-1):
        x=x[-i]+x
        continue
    return x

create_palindrome(input("enter string: "))
