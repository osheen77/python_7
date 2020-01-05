# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 14:41:47 2020

@author: Osheen
"""
print("Exercise 8.1")
def display_message():
# deffining message
 print("\nI am learning chapter 8")
#####################################################
display_message()

print("\nExercise 8.2")

def fav_book(book):
    print("The name of my favorite book is  " + book)

fav_book('Alice in wonderland')

#######################################################
print("\n8.3")

def make_shirt(size,message):
    print("The size of the shirt is " + size +" and the mesage on the shirt is " + message)
    
make_shirt('6','I love NY')

#######################################################

print("\n 8.4")

def make_shirt(size, message= 'I LOVE PYTHON'):
     print("The size of the shirt is " + size +" and the mesage on the shirt is " + message)
     
make_shirt(size='medium')
make_shirt(size='large')

def make_shirt(size,message):
    print("The size of the shirt is " + size +" and the mesage on the shirt is " + message)
make_shirt('XL', 'I am big')
make_shirt('XS', 'I am small')
 ######################################################
 
 
print("\n 8.5")
def describe_city(city,country='India'):
    print("\n" + city +" is in " + country)

describe_city('chandigarh')
describe_city('delhi')
describe_city('jammu')



describe_city(city='scranton', country ='USA')

#################################################################

print("\n 8.6")

def city_country(city,country):
    full = city + ' '+ country
    return full.title()

ready =city_country('"Penn"','"USA"')
print(ready)
ready =city_country('"Montana"','"USA"')
print(ready)   
ready =city_country('"Boston"','"USA"')
print(ready)

####################################################################

print("\n 8.7")

def make_album(artist,title, tracks=''):
    if tracks:
        info= { 'artist': artist, 'titile':title, 'tracks' :tracks }
    else:
        info = {'artist': artist, 'titile':title}
    return info
fin= make_album('bbnos', 'la la la')
print(fin)
fin= make_album('beyo', 'single ladies',4)
print(fin)

#######################################################################

print("\n 8.8")

def make_album(artist,title, tracks=''):
    if tracks:
        info= { 'artist': artist, 'titile':title, 'tracks' :tracks }
    else:
        info = {'artist': artist, 'titile':title}
    return info
while True:
    print("\ninformation for the song inquiry: ")
    print("Enter quit at any moment")
    
    artist_1= input("name of the artist is : ")
    if artist_1 == 'quit':
        break 
    
    title_1=input("title of the album is : ")
    if title_1== 'quit':
        break
    
    track_1=input("number of tracks : ")
    if title_1== 'quit':
        break
    fin= make_album( artist_1, title_1,track_1)
    print(artist_1 + "has the album : " + title_1 +" with tracks " +track_1) 

#######################################################################

print("\n 8.9")

def show_magician(names):
    for name in names:
        print("This is the name of magician: " +name.title())
magicians= ['rete', 'nukara', 'masu', 'himavari']
show_magician(magicians)
    
#######################################################################

print("\n 8.10")
def show_magician(names):
    for name in names:
        print("This is the name of magician: " +name.title())
magicians= ['rete', 'nukara', 'masu', 'himavari']
show_magician(magicians)


def make_great(namess):
    for name in namess:
        print("Great magician: " +name.title())
magicians= ['rete', 'nukara', 'masu', 'himavari']
make_great(magicians)

######################################################################

print("\n 8.11")
def make_great(namess):
    for name in namess:
        print("Great magician: " +name.title())

        return(name.title())
magicians= ['rete', 'nukara', 'masu', 'himavari']
print_now= make_great(magicians[:])
print(print_now)


def show_magician(names):
    for name in names:
        print("This is the name of magician: " +name.title())
magicians= ['rete', 'nukara', 'masu', 'himavari']
show_magician(magicians[:])

#####################################################################

print("\n 8.12")
def sandwich(*fillings):
    print("\n Add the following fillers in your sandwich; ")
    for filling in fillings:
        print("- " + filling)
sandwich('tuna')
sandwich('chicken','onion','tomatoes')
sandwich('tofu','mayo')

#######################################################################

print("\n8.13")

def build_profile(first,last,**info):
    profile={}
    profile['first name']=first
    profile['last name']=last
    for key,value in info.items():
        profile[key]=value
    return profile
user=build_profile('Osheen','Kaul',location='Carlton',degree='MEng'
                   ,hometown='Chandigarh')
print(user)

#######################################################################

print("\n8.14")

def make_car(name,model_type,**info):
    cars={}
    cars['model name']=name
    cars['model type']=model_type
    for i, j  in info.items():
        cars[i]=j
    return cars
car= make_car('Subaru','Outback',color='blue',Tow_package='True')
print(car)

#######################################################################






















