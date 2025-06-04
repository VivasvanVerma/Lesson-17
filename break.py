s = input("Enter a string: ")
s = s.lower()

for i in s:
    if i == "a":
        print("There is a letter a in ", s)
        break
    else:
        print("There is no letter a in ", s)