# 1
""" Write a program to calculate the credit card balance after one year if a person only pays the minimum 
monthly payment required by the credit card company each month. """

def interest(balance, MPR, APR):
    for i in range (12):
        balance = round((balance -(balance * MPR)), 2)
        balance = round((balance + balance * (APR / 12)), 2)
    return(balance)
        
print(interest(balance, monthlyPaymentRate, annualInterestRate))

# 2
""" Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid 
each month. """

increment = 10
monthlyPayment = increment

def interest(B, MP, APR):
    for i in range (12):
        B -= MP
        B = round((B + B * (APR / 12)), 2)
    return(B)
    
while True:
    if interest(balance, monthlyPayment, annualInterestRate) < 0:
        print(monthlyPayment)
        break
    else:
        monthlyPayment += increment
        
# 3
# Using Bisection Search to Make the Program Faster

low = balance / 12
high = (balance * (1 + annualInterestRate/12)**12) / 12
epsilon = 0.12

def interest(B, MP, APR):
    for i in range (12):
        B = round((B -(MP)), 2)
        B = round((B + B * (APR / 12)), 2)
    return(B)
    
while True:
    monthlyPayment = round(((high + low) / 2), 2)
    
    if abs(interest(balance, monthlyPayment, annualInterestRate)) < epsilon:
        print(monthlyPayment)
        break
    
    elif interest(balance, monthlyPayment, annualInterestRate) > 0:
        low = monthlyPayment

    else:
        high = monthlyPayment
