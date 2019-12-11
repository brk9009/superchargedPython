s = 'Hello'
ch = s[0]
print(type(ch))

# Removing the quotation marks using slicing
king_str = '"Henry VIII"'
new_str = king_str[1:-1]
#test_str = king_str[-4:]
print(new_str)
#print(test_str)

# Start at the character in 1st position and get every other character
# Returns ooo
a_str = 'RoboCop'
b_str = a_str[1::2]
print(b_str)

# Function to reverse a string. 
def reverse_string(s):
    return s[::-1]

print(reverse_string('Wow Bob wow!'))
print(reverse_string('Racecar'))

# Slicing out of bounds returns nothing
a_str = 'cat'
b_str = a_str[10:20]
print(b_str)