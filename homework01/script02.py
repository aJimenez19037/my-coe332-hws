import names

count = 0


while True:
    name = names.get_full_name()
    
    if (len(name) == 9):
        print (name)
        count+=1
    if (count == 5):
        break
    
