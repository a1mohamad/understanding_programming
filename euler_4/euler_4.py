

palindrome_number = []
for i in range(900000, 1000000):
    string = str(i)
    if string[0] == string [5]:
        if string[1] == string [4]:
            if string[2] == string[3]:
                number = int(string)
                palindrome_number.append(number)

palindrome_number.reverse()
for every in palindrome_number:
    for i in range(900, 1000):
        if every % i == 0:
            if 900 < every / i < 1000:
                print('%i * %i = %i' %(i, every/ i, every))

    
        


