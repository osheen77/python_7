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
    repeat=input("say yes or no ")
    if repeat == 'no':
        poll_active= False

for name,response in responses.items():
    print(name.title() + " would like to have number " + response)


####Dictionary for  the input of list####\

print("\n 7.8 Deli")
sandwich_orders = ['tuna', 'chicken', 'beef','pork']
finished_sandwich=[]

while sandwich_orders:
    working_sandwich=sandwich_orders.pop()

    print("The order for the " + working_sandwich + " is taken")
    finished_sandwich.append(working_sandwich)
    
for user in finished_sandwich:

    print("\nThe order for " + user + " is ready. ")
    
print("\nThese sandwiches are made: ")
for user in finished_sandwich:
    print(user)


################################################################
print("\n 7.9")

sandwich_available = ['tuna','pastrami', 'chicken','pastrami', 'beef','pastrami'
                      ,'pork']
finished_sandwich=[]

print(sandwich_available)
print ("Deli has run out of patrami ")

while 'pastrami' in sandwich_available:
    sandwich_available.remove('pastrami')
print("Now avaialble: ")
print(sandwich_available)
    

while sandwich_available:
    working_sandwich=sandwich_available.pop()

    print("The order for the " + working_sandwich + " is taken")
    finished_sandwich.append(working_sandwich)
        
print("\nThese sandwiches are made: ")
for user in finished_sandwich:
    print(user)
    
#########################################################
print("\n 7.10")

print("places to visit")
answers={}
poll_active=True

while poll_active:
    name=input("\nname of the participant ")
    place=input("place that you would like to visit ")

    answers[name]=place
    print("Would you like to add more ")
    new=input("any new place ")
    if new == 'no':
        poll_active=False

for name,place in answers.items():
    print(name.title() + " would like to visit " + place + ".")
    
    