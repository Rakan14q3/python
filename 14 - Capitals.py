mark=0
countries=["Saudi Arabia","Italy","Lebanon","Iraq","Egypt"]
Capitals=["Riyadh","Rome","Beirut","Baghdad","Cairo"]
for i in range(5):
    a=input("what is the capital of " +countries[i]).capitalize()
    if a==Capitals[i]:
        mark+=1
        print ('correct')
    else:
        print ('wrong The correct answer is',Capitals[i])
    
print ("Your score =",mark)
