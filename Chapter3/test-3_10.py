anything = ['me', 'time', 'China', 'Yellow', 'blue']

print(sorted(anything))
print(sorted(anything, reverse=True))

print(anything.pop())
anything.remove('time')
print(anything)

anything.insert(0, 'number')
print(anything)
print(len(anything))