
import math

def simple_inputs():
    print('How many years will you be investing?')
    years = int(input('Enter years: '))
    print('What is the principle amount?')
    principle = float(input('Enter amount: '))
    print('What will your yearly interest be on your investment?')
    interest = float(input('Enter your yearly interest rate: '))

    total_interest = (principle*years*interest)/100
    total = total_interest+principle

    print('Your total after {} years will be $'.format(years) + str(total))



def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result
 
def result1():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))
    
    amount = compound_interest(p, r, t)
    interest = amount - p
    print("Compound amount is %.2f" % amount)
    print("Compound interest is %.2f" % interest)

print('Would you like to calculate the simple interest, or compounding interest on the loan?')

def main():
    calculator = True
    while calculator:
        type_int = input(print('Enter "simple" or "compounding":'))
        if type_int.lower() == "simple":
            simple_inputs()
            calculator = False
        elif type_int.lower() == "compounding":
            compound_interest(0,0,0),
            result1()
            calculator = False
        else:
            print('That is not a valid entry.')
            
        

if __name__ == "__main__":
    main()


