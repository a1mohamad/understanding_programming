height = int(input())
weight = int(input())
height_in_meter = height/ 100
bmi = weight /(height_in_meter*height_in_meter)
if bmi < 18.5 :
    print('underweight')
if  25 > bmi >= 18.5 :
    print('ideal')
if bmi >= 25 :
    print('overweight')
