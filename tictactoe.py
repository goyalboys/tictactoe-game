def row_check(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            print a[i],"won"
            return 0
        elif b[i]==b[i+1]==b[i+2]:
            print b[i],"won"
            return 0
        elif c[i]==c[i+1]==c[i+2]:
            print c[i],"won"
            return 0   

def col_check(a,b,c):
    for i in range(3):
        if a[i]==b[i]==c[i]:
            print a[i],"won",
            return 0

def dia_check(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            print a[i],"won"
            return 0
        elif a[i+2]==b[i+1]==c[i]:
            print a[i],"won"
            return 0
 
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
print a
print b
print c
p1=raw_input("player 1 name")
p2=raw_input("player 2 nmae")
h=1
for i in range(9):
    if h==0:
        break
    if i%2==0:
        print p1 ,"turn"
        u=input()
        if u<=3:
            a[u-1]='x'
        elif u>3 and u<=6:
            b[u-3-1]='x'
        else:
            c[u-6-1]='x'
    else :
        print p2,"turn"
        u=input()
        if u<=3:
            a[u-1]='0'
        elif u>3 and u<=6:
            b[u-3-1]='0'
        else:
            c[u-6-1]='0'
    
    h=row_check(a,b,c)
    h=col_check(a,b,c)
    h=dia_check(a,b,c)
    print a
    print b
    print c
