names = ['yuri', 'sigma', 'tom', 'jerry']

for name in names:
    message = "Dear " + name.title() + ", I want to invite you for dinner."
    print(message)

name_absent = names.pop(0)
name_invited = "Lucy"
print(name_absent.title() + " is busy, he won't come this evening. "
                            "\nSo I invited " + name_invited + ".")
names.insert(0, name_invited)
names.sort()
print(names)

for name in names:
    message = "Dear " + name.title() + ", I want to invite you for dinner."
    print(message)
