def ispalindrome(a):
    pc=None
    for i,j in enumerate(a):
        if a[i]==a[-(i+1)]:
            pc=True
            continue
        else:
            pc=False
            break
    return pc

ispalindrome(input())
