# Bad way to add to strings. Creates a new string in every loop.
# Prints the alphabet.
n = ord('A')
s = ''
for i in range(n, n + 26):
    s += chr(i)
print(s)

# More efficient way at concatenating a string with join. 
n = ord('A')
a_lst = []
for i in range(n, n + 26):
    a_lst.append(chr(i))
s = ''.join(a_lst)
print(s)

# Prints a list of names one string at a time.
def print_nice(a_lst):
    s = ''
    for item in a_lst:
        s += item + ', '
    # Get rid of trailing comma
    if len(s) > 0:
        s = s[:-2]
    print(s)

print_nice(['John', 'Paul', 'George', 'Ringo'])

# Print a list of names using the join method
def print_nice2(a_lst):
    print(', '.join(a_lst))

print_nice2(['John', 'Paul', 'George', 'Ringo'])
