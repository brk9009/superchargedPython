# my_lst doesn't get affected by for loop
my_lst = [10,15,25]
for thing in my_lst:
    thing *= 2
    #print(thing)

print("Unaffected list: " + str(my_lst))

# double each element in list
my_lst = [10,15,25]
for i in [0, 1, 2]:
    my_lst[i] *= 2
print("Affected list: " + str(my_lst))

# Best way to double list
my_lst = [100, 102, 50, 25, 72]
for i in range(len(my_lst)):
    my_lst[i] *= 2
print("Best way to double list: " + str(my_lst))
