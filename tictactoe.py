import time
print" 1 | 2  | 3"
print"_________________"
print" 4 | 5  | 6" 
print"_________________"
print" 7 | 8  | 9"

print("what do you want to take 0 and X")


p1=raw_input()
if p1=='X':
    print " player1 is X:"
    p2='0'
else:
    print "player 2 is 0:"
if p1=='0':
    print "player 1 is 0"
draw=0
chance=0
p=[' ',' ',' ', ' ', ' ',' ',' ',' ',' ']
while chance<9:
    print" ",p[0]," | ",p[1],"  | ",p[2] 
    print"______________________"
    print" ",p[3]," | ",p[4],"  | ",p[5] 
    print"______________________"
    print" ",p[6]," | ",p[7],"  | ",p[8] 
   
    k=1
    chance+=1
    if chance%2==0:
        while k:
            print "player 1 turn"
            i=input()
            if i<=9 and p[i-1]==' ':
                p[i-1]='X'
                k=0
            else:
                print "invalid entry" 
    else:
        while k:
            print "player 2 turn"
            i=input()
            if i<=9 and p[i-1]==' ':
                p[i-1]='0'
                k=0
            else:
                print "invalid entry"
    if p[0]==p[1]and p[1]==p[2] and p[0]!=' ':
        draw=1
        if p[0]=='X':
            print "player  one won"
            break
        else:
            print "player two won"
            break
    if p[0]==p[3]and p[3]==p[6]and p[0]!=' ':
        draw=1
        if p[0]=='X':
            print "player one won"
            break
        else:
            print "player two won"
            break
    if p[0]==p[4]and p[4]==p[8]and p[0]!=' ':
        draw=1
        if p[0]==1:
            print "player one won"
            break
        else:
            print "player two won"
            break
    if p[2]==p[5]and p[5]==p[8]and p[2]!=' ':
        draw=1
        if p[0]==1:
            print "player one won"
            break
        else:
            print "player two won"
            break
        
    if p[6]==p[7]and p[7]==p[8]and p[7]!=' ':
        draw=1
        if p[0]=='X':
            print "player one won"
            break
        else:
            print "player two won"
            break
    if p[2]==p[5]and p[5]==p[8]and p[2]!=' ':
        
        draw=1
        if p[0]=='X':
            print "player one won"
            break
        else:
            print "player two won"
            break
    if p[4]==p[5]and p[5]==p[6]and p[4]!=' ':
        draw=1
        if p[0]=='X':
            print "player one won"
            break
        else:
            print "player two won"
            break
    

if draw==0:
    print "draw"

time.sleep(7)      
    
        
        
        
    


