"""A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the
same and the middle is a palindrome.The following are functions that take a string
argument and return the first, last, and middle letters:

def first(word):
return word[0]
def last(word):
return word[-1]
def middle(word):
return word[1:-1]

1. Type these functions into a file named palindrome.py and test them out. What
happens if you call middle with a string with two letters? One letter? What
about the empty string, which is written “” and contains no letters?
#answer: when we call the middle with a string of two letters,one letter or no letter,then it returns a empty value.

2. Write a function called is_palindrome that takes a string argument and returns
True if it is a palindrome and False otherwise. Remember that you can use
the built-in function len to check the length of a string."""


#Question number 1 solution.
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

word=input("Enter a word: ")

#checking the length of the word for finding the middle letter.
if len(word)=="":
    middle(word)
    print ("no input given",middle(word))
elif len(word)==2:
    middle(word)
    print("cannot find the middle letter ",middle(word))
elif len(word)==1:
    middle(word)
    print("only one letter is given,cannot find middle value ",middle(word))
elif len(word)>2:
    middle(word)
    print( middle(word))

print("\nSolution for question number two\n")

#Question number 2 solution.checking whether a given word is palindrome or not.
def _palindrome(word1):
    strword=str(word1)
    txtval=strword[::-1]
    if strword== txtval:
        return True
    else:
        return False
    
word1=input("Enter a word: ")
reval=word1[::-1]
pvalue= _palindrome(word1)
if pvalue == True:
    print ("Yes",word1, "is a palindrome because its reverse is", reval , "which is the same as the original word",word1)
else:
    print ("No",word1, " is not a palindrome because its reverse is", reval , "which is not same as the original word",word1)
    
    
    

    
    
