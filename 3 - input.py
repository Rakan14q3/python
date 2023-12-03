username=input("what is your name")
print ("hello",username)
#int is a function that converts values to integer
per_hour=int(input("price per hour"))
work=int(input("number of hours"))
salary=per_hour*work
tax=salary*0.05
net_salary=salary-tax
print (username,"- your salary:",net_salary)
