for i in range(10):
    import random
    R=random.randint(1,10)
    w=random.randint(1,10) 
    s=R*w
    print (R,"x",w)
    y=int(input("="))
    if y==s:
        print ("correct")
    else :
        print ("not correct") 
#Hw : 1 point for each correct answer and print the score
