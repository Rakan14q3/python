q=input("who is the best player in the world").lower()
if q== "messi":
    mark=1
    print ("correct")
else:
    mark=0
    print("sorry you're idiot")

q=input("who is the second player in the world").lower()
if q== "cr7":
    mark+=1
    print ("correct")
else:
    print("sorry you're idiot")

q=input("who is the best team in the world").lower()
if q== "Real Madrid":
    mark+=1
    print ("correct")
else:
    print("sorry you're idiot")

print ()
print ("Your score =",mark)
#homework add two more questions and print "the score out of 5"
    
