def get_int(msg = "Enter a number: "):          #Define the input as a float and reject anything that is not a number
    try:
        inp = float(input(msg))
    except ValueError:
        print("Please enter a number... ")
        inp = get_int(msg)
    return inp

#Compound Interest Calculator

P = get_int("How much are you investing?  ")                        #Initial investment
print(f'You entered ${P}!')
r = get_int('What is your interest rate? (eg. 3.25)  ')            #Rate of return
rr = r/100
print(f'You entered {r}%')
n = get_int('How many times per year is interest compounded?  ')     #How many months in a year is the interest compounded? ex: n/12
print(f'You entered {n} times per year.')
t = get_int('Years invested:  ')                                     #How long, in years, is the investment being made?
print(f'You entered {t} times per year')

A = P * (( 1 + rr/n ) **(n*t))                                       #Formula to figure out total after investment
T = A - P                                                           #Subtratcting to get only the interest returned

T = round(T, 2)                                                     #Rounding to the hundreth decimal point
A = round(A, 2)

print('You invested $' + str(P) + ' at ' + str(r) + '% interest and earned $' + str(T) + ' for a total of $' + str(A) + '!')

exit = input("Press the enter key to exit") #Give the user time to see their results before the window closes
