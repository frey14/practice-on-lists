'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

forw=input("Enter your string")
forw=str(forw)
rev=forw[::-1]
print(rev)
if forw==rev:
    print("the given string",forw,"is a palindrome")
else:
    print("the given string",forw,"is not a palindrome")
    
