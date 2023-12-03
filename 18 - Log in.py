Usernames=["Rawan","Rakan","Hadia"]
Passwords=["R1","R2","H3"]
a=input("What is the Username?")
if a in Usernames :
    b=input ("what is the passwords?")
    index1=Usernames.index(a)
    if b in Passwords :
        index2=Passwords.index(b)
        if index1==index2:
            print ("welcome")
        else :
            print ("access denied")
    else:
        print ("access denied")
else:
    print ("this user dose not exist")
