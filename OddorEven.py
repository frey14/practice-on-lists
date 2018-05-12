'''Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.'''

num=input("dear user enter a number of your choice")
num=int(num)
if(num%2==0):
    print("the given number",num,"is an even number")
else:
    print("the given number",num,"is an odd number")
    
