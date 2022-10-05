import random as r
from time import *

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput) / time_r
    return round(speed)

if __name__ == '__main__':
    while True:
        inp = input("Would you like to start your test : yes / no : ")
        if inp.lower() == 'yes':
            test = ['A demo paragraph', 'Another nice paragraph', 'again another paragraph']
            test_select = r.choice(test)
            print('******* typing speed *********')
            print(test_select, '\n \n')
            time_s = time()
            userinput = input(" Enter : ")
            time_e = time()
            print('Speed : ', speed_time(time_s, time_e, userinput))
            print('Error : ', mistake(test_select, userinput))
        elif inp.lower() == 'no':
            print('Thank for being with us')
            break
        else:
            print('Enter a valid input')