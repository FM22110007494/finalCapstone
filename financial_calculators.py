import math
print ("ivestment - to calculate the amount of investment you will earn o your investments")
print ("bond - to calculate the amount you will have to pay on a home loan")
print ("enter either 'investments' or 'bond' from the menu above to proceed:")

calculator = input ("enter 'investment' or 'bond calculator:").lower() # the user is asked to choose one of the calculator type
if calculator == 'investment': # for investment calculator it will prooced the code and the formula below :
  principal_deposite = float(input("Please enter the amount of money you want to deposit:") )
  interest_rate = float (input("Please enter the interest rate (as a percentage):") )/12 /100
  years = int(input("Enter the number of years:"))
  interest = input("simple' or 'compound: ") # because are two types of interest for investment calculator, the user is asked to choose if simple or compound

  if interest == 'simple':
    total_simple_amount = principal_deposite * (1 + interest_rate * years)
    print(total_simple_amount)
  elif interest == 'compound':
    total_compound_amount = principal_deposite * math.pow((1 + interest_rate), years)
    print(total_compound_amount)
  else:
      print("error")
      
elif calculator == 'bond':# if user choose bond calculator will prooced the following code and the formula below:
  present_value = float(input("Enter the present value of the house:"))
  interest_rate = float(input("enter interest rate:"))
  months = int(input("number of months:"))
  repayment = (interest_rate * present_value) / (1 - (1 + interest_rate)**(-months))
  print(repayment)
else:
  print("error: Please eneter investment or bond ")
  
