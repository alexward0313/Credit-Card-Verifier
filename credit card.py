import math
import numpy


number = input(str("Please Input Credit Card Number: "))
 
if (len(number) > 13) and (len(number) < 17):
    #splits the digits into a list of integers
    digits = list(int(c) for c in number)
    #takes every other digit starting at place 0
    e = [digits[index] for index in filter(lambda x: x % 2 == 0, range(len(digits)))]
    #takes every other digit starting at place 1
    ea = [digits[index] for index in filter(lambda x: x%2 == 1, range(len(digits)))]
    #get the sum of ea
    fa = sum(ea)

    #multiply every number in e by 2
    ex = [i * 2 for i in e]

    #in order to seperate all the digits from the integers we need to combine all the integers into one big integer
    tex = int("".join(map(str, ex)))
    #then we split them apart again into single digit integers
    rex = [int(a) for a in str(tex)]
    #finally we add them all together
    f = sum(rex)
    
    #adds f and fa together
    total = f + fa
    #gets the last digit of the total
    last_digit = int(repr(total)[-1])
    #if the last digit is 0 then its valid else its invalid
    if last_digit == 0:
        print("This Credit Card Number is Valid")
    else:
        print("This Credit Card Number is Invalid")
else:
    print("Invalid Credit Card Number")

    

    

    