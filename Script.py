#integer int


#Ask user 
Name = input ("What is your name?/n").title().strip()

#Remove space
#Name = Name.strip()

#Capitalize only first letter
#Name = Name.capitalize()

#Capitalize First letter of the word
#Name = Name.title()

#Split the Name
first, last = Name.split (" ")
#Print it 
print(f"Hello  {first}")
#print(Name) 