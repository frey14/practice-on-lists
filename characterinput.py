'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.'''

name=input("Dear user Enter your name");
age=int(input("Enter your age also"));
lifetime=100-age+2018
print("Dear",name,"you will complete your 100 years by",lifetime)
