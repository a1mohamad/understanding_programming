from docx import Document
def persian_num_to_english_num (string):    #in this function we change persian number to english number
    list1 = list(string)
    for i in range(len(list1)):
        if list1[i] == '۰':
            list1[i] = '0'
        elif list1[i] == '۱':
            list1[i] = '1'
        elif list1[i] == '۲':
            list1[i] = '2'
        elif list1[i] == '۳':
            list1[i] = '3'
        elif list1[i] == '۴':
            list1[i] = '4'
        elif list1[i] == '۵':
            list1[i] = '5'
        elif list1[i] == '۶':
            list1[i] = '6'
        elif list1[i] == '۷':
            list1[i] = '7'
        elif list1[i] == '۸':
            list1 [i] = '8'
        elif list1 [i] == '۹':
            list1[i] = '9'
        elif list1[i] == '٬':
            list[i] ='.'
        elif list1[i] == '٫':
            list1[i] ='.'
        elif list1[i] == '،':
            list1[i] = '.'
    english_number = ''.join(list1)
    return english_number

def number_back(string):    #in this function,we return numbers of a string
    string_2 = string + '!'
    each_number = ''
    numbers = []
    for i in range(len(string)):    #add numbers in a list subject loop
        if string[i] in '0.123456789۰۱۲۳۴۵۶۷۸۹٬٫،':
            if string_2[i+1] in '0123456789.۰۱۲۳۴۵۶۷۸۹٬٫،':
                each_number += string[i]
            else :
                each_number += string[i]
                if each_number == '.':
                    each_number = ''
                elif each_number == '٬':
                    each_number = ''
                elif each_number == '٫':
                    each_number = ''
                elif each_number == '،':
                    each_number = ''
                else:    
                    numbers.append(each_number.strip())
                    each_number = ''
    
    for i in range(len(numbers)):    #correctioning outliers datas
        if numbers[i][0] == '.':
            numbers[i] = numbers[i][1:]
        elif numbers[i][-1] == '.':
            numbers[i] = numbers[i][:-1]
        elif numbers[i][0] == '٬':
            numbers[i] = numbers[i][1:]
        elif numbers[i][-1] == '٬':
            numbers[i] = numbers[i][:-1]
        elif numbers[i][0] == '٫':
            numbers[i] = numbers[i][1:]
        elif numbers[i][-1] == '٫':
            numbers[i] = numbers[i][:-1]
        elif numbers[i][0] == '،':
            numbers[i] = numbers[i][1:]
        elif numbers[i][-1] == '،':
            numbers[i] = numbers[i][:-1]
                    
    
    for i in range(len(numbers)):    #changing persian numbers to english ones
        if numbers[i][0] in '۰۱۲۳۴۵۶۷۸۹':
            numbers[i] = persian_num_to_english_num(numbers[i])
            
    for i in range(len(numbers)):    #returning float numbers to mathematical operation
        numbers[i] = float(numbers[i])
    
    return numbers

def sum_number_in_text(input_filename):    #this function transforming  a docx file to string and returning sum numbers in it
    input_filename = str(input_filename)
    doc = Document(input_filename)
    reading = ''
    for para in doc.paragraphs:
        reading += para.text
    
    final_sum = sum(number_back(reading))
    return print(final_sum)

sum_number_in_text('./tiger.docx') #this is my prototype file direction of your file
                                                                        #use yours :))))
                
        
        
