#using string reversal

wrd=input("Please enter a word") #get input from user
wrd=str(wrd) #validate that its a string 
rvs=wrd[::-1] #reverse the string
print(rvs)
if wrd == rvs: #if the string is the same as the reversed version it is a palindrome
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")


# palindrome using for loops

def reverse(word):   #function to reverse the word
	x = ''  #set x to empty string
	for i in range(len(word)):  #loop throught the len of the given word
		x += word[len(word)-1-i] #add character to string starting from last
		return x

word = input('give me a word:\n') #user input to give word
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')