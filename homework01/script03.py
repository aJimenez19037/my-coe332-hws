import names

count = 0


while True:
    name = names.get_full_name()
    print(name, end ="")
    print(" ", end = "")
    name = name.replace(" ", "")
    print(len(name))
    count+=1
    if (count == 5):
        break
