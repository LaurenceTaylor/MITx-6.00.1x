# 1
/* Write a program to calculate the credit card balance after one year if a person only pays the minimum 
monthly payment required by the credit card company each month. */

def interest(balance, MPR, APR):
    for i in range (12):
        balance = round((balance -(balance * MPR)), 2)
        balance = round((balance + balance * (APR / 12)), 2)
    return(balance)
        
print(interest(balance, monthlyPaymentRate, annualInterestRate))
