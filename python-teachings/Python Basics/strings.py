#Strings

message = """Bob's World
is a great place to visit!"""

print(message)

#Advanced concepts in strings

message = 'Hello'

print(message[0]) #H
print(message[1]) #e    
print(message[-1]) #l
print(len(message)) #5

#More Advanced concepts in strings

message = ' Hello, World! '

print(message.lower()) # hello world!
print(message.upper()) # HELLO WORLD!
print(message.strip()) # Removes whitespace from start and end
print(message.replace('H', 'J')) # Jello World!
print(message.split(',')) # Split the string into list based on comma
