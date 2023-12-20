from math import pi
def realestate():
    norooms = int(input('How many rooms does the floor have? '))
    length = dict()
    width = dict()
    for i in range(realestate):
        length[i] = input('what is the length of room? ')
        width[i] =input('what is the width of room? ')
        print('that was room number:',i+1)
    total=0
    for i in range(realestate):
        total += float(length[i])*float(width[i])

    print ('Total is:' ,total)


# def calculate_cir(radius):
#     return round(2 * pi * radius, 2)
        
