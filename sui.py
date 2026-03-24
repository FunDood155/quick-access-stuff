import random 

def place(ele_to_place):
    x=random.randint(0,8)

def display():
    i=1
    jj=1
    for j in l:
        # print(str(j[0:3])[1:8],str(j[3:6])[1:8],str(j[6:9])[1:8],sep=" | ")
        print(j[0]," " ,j[1]," " ,j[2]," | ",j[3]," " ,j[4]," " ,j[5]," | ",j[6]," " ,j[7]," " ,j[8])
        if(i==3 and jj<3):
            print("- - - - - - - - - - - - - - - - - - -  ")
            i=0
            jj+=1
        i+=1

l=[]
temp_l=[0]*9
for i in range (9):
    l.append(temp_l)
#taking rows
r1=l[0];r2=l[1];r3=l[2];r4=l[3];r5=l[4];r6=l[5];r7=l[6];r8=l[7];r9=l[8]
display()