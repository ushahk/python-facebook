def palindrome_center(c):
    p={}
    if len(c)%2!=0:
        for i in range (1,len(c)-1):
            for j in range(1,len(c)):
                if i-j>-1 and i+j<len(c) and c[i-j]==c[i+j]:
                    p[i]=j
                else:
                    break
    else:
        for i in range (len(c)):
            for j in range(1,int(len(c)/2),1):
                if i-j>-1 and i+j<len(c) and c[i]==c[i-1]:
                    p[i-1]=j
                else:
                    break
    print(p)
    return p


def marker_palindrome(x):
    meta_dict=palindrome_center(x)
    ld=len(meta_dict)
    if ld%2!=0:
        center=int(ld/2)+1
    else:
        center=ld/2
    pc=-1
    meta_keys=list(meta_dict.keys())
    for i,j in enumerate(meta_keys):
        if i>0 and meta_keys[i]-meta_keys[i-1]==1:
            pc=i
        else:
            continue
    print(pc)
    return pc


def create_palindrome(x):
    mark=marker_palindrome(x)
    palindrome=''
    for i in range(mark+1,len(x)):
        palindrome=x[i]+x
        continue
    return palindrome

# def frange(sta,sto,jmp):
#     v=[]
#     while sta<sto:
#         v.append(sta)
#         sta+=jmp
#     return v


create_palindrome(input("enter string: "))
