#using string reversal

wrd=input("Please enter a word") #get input from user
wrd=str(wrd) #validate that its a string 
rvs=wrd[::-1] #reverse the string
print(rvs)
if wrd == rvs: #if the string is the same as the reversed version it is a palindrome
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")