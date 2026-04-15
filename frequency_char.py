###Frequency of a specific character
##string=input("Enter a string:")
##char=input("Enter a character:")
##
##count=0
##for c in string:
##    if c==char:
##        count+=1
##print(f"Frequencys of '{char}' is:",count)


###Using built_in fuction (simple)
##a=input("Enter a string:")
##char=input("Enter a character:")
##
##print("Frequency:",a.count(char))


#Frequency of all character in a string(using dictonary)
string=input("Enter a string:")
frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print("Character frequencies:")
print(frequency)
