#Darron Smallwood September 20, 2017
#Program calculates the sales tax for MD, VA, DC


#Vars Needed for the Program
userName = input("Please type in your first name ")
userTotalPrice = float(input("Please type in your total amount "))
stateSaleTax = 0.00
userState = input("Please enter the two letters of your state ")

if userState == "MD":
    stateSaleTax = 0.06
    print(userTotalPrice * stateSaleTax + userTotalPrice)

if userState == "VA":
    stateSaleTax = 0.053
    print(userTotalPrice * stateSaleTax + userTotalPrice)


if userState == "DC" :
    stateSaleTax = 0.0575
    print(userTotalPrice * stateSaleTax + userTotalPrice)

else:
    print("Sorry,that state's sales tax isn't in our system.")
