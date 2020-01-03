# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:09:24 2019

@author: Osheen
"""
#######chapter 7###############

enter=input("type your message here: ")
print(enter)

age=input("how old are you ")
ans=int(age)
print(ans)

print("7.1")
car=input("what kind of car do you want: ")
print("Let me look for it")

print("\n7.1")
guest=input("\nHow many guests do we need to book for: ")
guest=int(guest)

if guest > 8 :
    print("You will have to wait for the table")
else:
    print("The table is ready")


#######prcatice while loop#########

r="\n type the messge here"
r += "\n or type quit: "

message= " "
while message != quit:
    message=input(r)
    
    if message == 'quit':
      break
    else:
        print(message)

print("\n 7.4")
prompt ="\n you will add this stopping : " 

entry=" "
while entry != 'quit':
    entry =input(prompt)
    
    if entry !='quit':
        print(entry)
 

print("7.5")     
prompt= "\nwhat is your age: "

active = True
while active:
        
    age = input(prompt)
    age =int(age)
    if age >100:
        active = False 
    elif age <=3:
        print("Ticket is free")
    elif age <=12:
        print(" Ticket is $10")
    elif age >12:
        print(" Ticket is $15")
  
    
print("\n7.6")
print("\n It is a conditional test")
prompt= "\nwhat is your age: "

active = True
while active:
        
    age = input(prompt)
    age =int(age)
    if age >100:
        active = False 
    elif age <=3:
        print("Ticket is free")
    elif age <=12:
        print(" Ticket is $10")
    elif age >12:
        print(" Ticket is $15")

print("\nNumber of times the program runs"

count =1
while count <= 3:
    prompt= "\nwhat is your age: "
    active = True
    while active:
        
        age = input(prompt)
        age =int(age)
        if age >100:
            active = False 
        elif age <=3:
            print("Ticket is free")
        elif age <=12:
            print(" Ticket is $10")
        elif age >12:
            print(" Ticket is $15")
    count +=1
 

prompt= "\nwhat is your age: "
prompt +="\nor type quit"
age = input(prompt)
while age !='quit':
      
    num = 0
    while num <2:
        age =int(age)
        if age <=3:
            print("Ticket is free")
        elif age <=12:
            print(" Ticket is $10")
        elif age >12:
            print(" Ticket is $15")

print("7.7")
print("don't rin its a infinite loop")

v=1
while True:
    print(v)
    v +=1
    
    
    
    
    #############Practice###########
    
# Movin  th eitems from one list to the other
unconfirmed_user =['eric','ray','matt']
confirmed_user=[]

while unconfirmed_user:
    current_user=unconfirmed_user.pop

print("The user: " + current_user.title() +" is being verified." ) 
confirmed_user=curremt_user.apped

for users in confirmed_user:
    print("\nThe user : " + users.titl() +" is verified." )
    
#############Exercise 7.8########################

responses={}

poll_active =True

while poll_active:
    name= input("\n what is your name ")
    response=input("\n fav number: ")

    responses[name]=response

    print("\n continue poll ")
    repeat=input("say yes\no ")
    if repeat == 'no':
        poll_active= False

for name,response in responses.items():
    print(name.title() + " would like to have number " + response)


####Dictionary for  the input of list####




    