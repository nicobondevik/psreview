#TODO
#check if word is in password

import sys
import string
import enchant
import getpass

def main():
    result = 0
    digits = 0
    upper = False
    digit = False
    pswd = str(sys.argv)
    #pswd = getpass.getpass(prompt = 'Password: ')
    pswd_length = len(pswd)

    d = enchant.Dict('en_US')
    if d.check(pswd) == True:
        result -= 10
        #print('word found!')

    i = 0
    while i < pswd_length-1:
        if pswd[i] != pswd[i+1]:
            result += 1

        for x in string.punctuation:
            if x == pswd[i]:
                #print(f'punctuation found at {i}')
                result += 1

        if pswd[i].isupper():
            upper = True
            result += 1
            #print('contains uppercase')

        if pswd[i].islower():
            lower = True

        if pswd[i].isdigit():
            digit = True
            result += 1
            digits += 1
            #print('contains number')

        i += 1

    if pswd_length > 8:
        result += 5

    if upper and lower and digit:
        result += 5

    if digits > pswd_length/3:
        result += 2

    result = result/pswd_length

    if result > 1.7:
        print('strong password')

    elif result < 1.7:
        print('weak password')

    print(f'{result}')
main()