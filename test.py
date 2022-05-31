import itertools

mytuple = ("apple", "banana", "cherry")
cy = itertools.cycle(mytuple)
#print(len(mytuple))
i = 1
for val in cy:
    print(val)
    i += 1
    if i > len(mytuple):
        break   
