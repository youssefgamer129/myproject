#Typing speed calculator
from _typeshed import ReadableBuffer


print("|-------------- Welcome to the typing speed calculator --------------| (:  ")
#Get input from user
words =int(input("Enter the words you typed: "))
print('Enter the time taken to type the words: ') 
hours= float(input("Enter hours :") )
minutes = float(input("Enter minutes :"))
seconds = float(input("Enter seconds :"))
#Convert time to hours
Hours= hours + minutes/60 + seconds/3600
Minutes= hours*60 + minutes + seconds/60
#Calculate typing speed
speed = words/Hours 
print( "\033[32m" + "Your typing speed is " + "\033[0m" ,speed," words per hour")
speed= words/Minutes
print( "\033[32m" + "Your typing speed is " + "\033[0m" ,speed," words per minute")
 

