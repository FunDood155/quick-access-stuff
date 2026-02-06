import random
import numpy as np

def place():
    a=random.randint(0,8)
    ans=1
    while(ans==1):
        if(a not in p):
            p.append(a)
            l[a]=1
            ans=0
        else:
            a=random.randint(0,8)
            ans=1

def get():
    a=int(input("Enter your position :"))
    #a=a+1
    ans=1
    while(ans==1):
        if(a not in p):
            p.append(a)
            l[a]=2
            ans=0
        else:
            a=int(input("Enter your position :"))
            ans=1

def display():
    b=0
    for i in range(3):
        for j in range(3):
            print(l[b]," ",end="")
            b=b+1
        print("\n")

def check():
    for i in wl:
        x,y,z=i[0],i[1],i[2]
        #print(x,y,z)
        if(l[x]==2 and l[y]==2 and l[z]==2):
            w=1
            print("\nYou WoOon.....:D")
            return w
        if(l[x]==1 and l[y]==1 and l[z]==1):
            print("\nYou LOST.....:(")
            w=1
            return w
        elif(min(l)!=0):
            w=0
            print("\nYou draw.....")
            return w
    else:
        w=0
        return w

###     MAIN        ###

l=[0,0,0,0,0,0,0,0,0]
p=[]
w=0
wl=np.array([0, 3, 6, 1, 4, 7, 2, 5, 8, 6, 7, 8, 3, 4, 5, 0, 1, 2, 6, 4, 2, 0, 4, 8])
wl=wl.reshape(8,3)
wl=[[0,3,6],[1,4,7],[2,5,8],[6,7,8],[3,4,5],[0,1,2],[6,4,2],[0,4,8]]



while(w==0):
    place()
    display()
    get()
    #display()
    w=check()
    #print("w : ",w)
print("\nTHE END.....")
