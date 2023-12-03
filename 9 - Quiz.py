q=input("who is the best player in the world").lower()
if q== "messi":
    mark1=1
    print ("correct")
else:
    mark1=0
    print("sorry you're idiot")

q=input("who is the second player in the world").lower()
if q== "cr7":
    mark2=1
    print ("correct")
else:
    mark2=0
    print("sorry you're idiot")

q=input("who is the best team in the world").lower()
if q== "Real Madrid":
    mark3=1
    print ("correct")
else:
    mark3=0
    print("sorry you're idiot")

print ()
print ("Your score =",mark1+mark2+mark3)
    
