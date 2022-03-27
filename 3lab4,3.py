#q3 lab4 and 3
s= str(input( "Enter a string: ").casefold())
if list(s)== list(reversed(s)):
    print("The given string(",s.title(),")is a palindrome.")
else:
    print("Sorry, the given string(",s.title(),")is not a palindrome.")
