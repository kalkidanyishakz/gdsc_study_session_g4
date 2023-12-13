name=input("Enter a name: ")

print(len(name))
print(name.upper())

if 'smith' in name.lower():
    print(f"{name} contains smith")
else:
    print(f"{name} doesn\'t contain smith")
    