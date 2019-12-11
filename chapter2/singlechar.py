# Check if the first character in s is a vowel
s = 'elephant'
if s[0] in 'aeiou':
    print('First char. is a vowel.')

# Check if the first char. is a consonant
s = 'Helephant'
if s[0] not in 'aeiuo':
    print('First char. is a consonant.')

# Case insensitive comparison
s = 'elephant'
if s[0].upper() in 'AEIOU':
    print('First char. is a vowel.')

print('' in 'cat') # Prints True
print([] in [1,2,3]) # Prints False

# Loop through string and find the type of the character.
s = 'Cat'
for ch in s:
    print(ch, ', type:', type(ch))