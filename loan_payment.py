loan_amount = 1000.0
annual_interest_rate = 18.0
monthly_payment = 180.0
debt_paid = 0
interest_paid = 0
month = 0
total_interest = 0
n = 1

print("Welcome to the Loan Payment Report of Jumai B!")
print(n,"=========================================================.") 
n+=1
print("Loan amount: $",loan_amount, "      Annual Interest Rate: ",annual_interest_rate, "%       Monthly Payment: $",monthly_payment)
print("Month      Month-Payment      Interest-Paid      Debt-Paid      Loan-Balance")
print("---------  -----------------  -----------------  -------------- -------------------")
while loan_amount >= monthly_payment:
    
    interest = annual_interest_rate/12
    pay = (interest * 10) / 1000
    interest_paid = pay * loan_amount
    debt_paid = monthly_payment - interest_paid
    loan_amount = loan_amount - debt_paid
    month += 1
    print ("%-2d" % month + "         $%0.2f" % monthly_payment + "              $%0.2f" % interest_paid 
          + "             $%0.2f" % debt_paid + "             $%0.2f" % loan_amount  ) 
    total_interest = total_interest + interest_paid
print("Total Amount of Interest Paid: ",total_interest)