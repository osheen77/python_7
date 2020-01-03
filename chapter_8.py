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





























