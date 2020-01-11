frank_str = 'doo be doo be doo...'

n = frank_str.count('doo')
print(n)
# Starts at the 2nd char and counts # of 'doo'
print(frank_str.count('doo', 1)) 
# Starts at the 2nd char and goes to 9th position
print(frank_str.count('doo', 1, 10))

# Uses find to find where all 'doo' starts at.
frank_str = 'doo be doo be doo...'
n = -1
while True:
    n = frank_str.find('doo', n + 1)
    if n == -1:
        break
    print(n, end=' ')

# Replace first with 2nd string every time.
title = '25 hues of Grey'
new_title = title.replace('Grey', 'Gray')
print()
print(new_title)
