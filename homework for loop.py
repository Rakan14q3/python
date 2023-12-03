mark=0
import random
for i in range(10):
    R=random.randint(1,10)
    w=random.randint(1,10) 
    s=R*w
    print (R,"x",w)
    y=int(input("="))
    if y==s:
        mark+=1
        print ("correct")
    else :
        print ("not correct,the answer is",s)



print ("Your score =",mark)
