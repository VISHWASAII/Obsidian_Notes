#String Method
#str datatype ah several method
name = input('Enter the input')
print(f"this is your name {name}")

#Remove whitespace from str
name = name.strip()
print(f"this is your name {name}")


#Capitalize the str
name = name.capitalize()
print(f"this the your name {name}") 

#Title the str
name = name.title()
print(f"this is your name {name}")

#we can provide all together
name = name.strip().title()
print(f"this is your name {name}")


#Or we can assign it in user input
name = input('Enter the input').strip().title()
print(name)