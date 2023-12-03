Usernames=["Rawan","Rakan","Hadia"]
Passwords=["R1","R2","H3"]
a=input("What is the Username?")
if a in Usernames :
    for i in range (3) :
        if a==Usernames[i]:
            print ('correct',Passwords[i])
else:
    print ("this user dose not exist")
