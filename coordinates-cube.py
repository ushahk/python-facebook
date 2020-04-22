if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    def __init__(self,x,y,z,n):
        x=self.x
        y=self.y
        z=self.z
        n=self.n

    def cordnt(x,y,z,n):
        cor=[]
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    if i+j+k!=n:
                        cor.append([i,j,k])
        return cor

    print(cordnt(x,y,z,n))
