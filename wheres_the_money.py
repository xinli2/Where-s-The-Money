###
### Author: Xin Li
### Description:  In this PA, you will be writing a program
### that helps a user visualize and understand how much money
### they spend of various categories of expenditures.
### Perhaps you will even find this program useful for your personal finances!
### Name of this program is: wheres_the_money.py
###
print('''-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------''')
from os import _exit as exit
salary = input('What is your annual salary?\n')
if salary.isnumeric()==True :
    salary=float(salary)
else:
    print('Must enter positive integer for salary.')
    exit (0)
if salary < 0 :
    print('Must enter positive integer for salary.\n')
    exit(0)

rent = input('How much is your monthly mortgage or rent?\n')
if rent.isnumeric()==True :
    rent=float(rent)
else:
    print('Must enter positive integer for mortgage or rent.')
    exit(0)
if rent < 0 :
    print('Must enter positive integer for mortgage or rent.')
    exit(0)

bills = input('What do you spend on bills monthly?\n')
if bills.isnumeric()==True:
    bills=float(bills)
else:
    print('Must enter positive integer for bills.')
    exit(0)
if bills < 0 :
    print('Must enter positive integer for bills.')
    exit(0)

food = input('What are your weekly grocery/food expenses?\n')
if food.isnumeric()==True:
    food=float(food)
else:
    print('Must enter positive integer for food.')
    exit(0)
if food < 0 :
    print('Must enter positive integer for food.')
    exit(0)

travel = input('How much do you spend on travel annually?\n')
if travel.isnumeric()==True:
    travel=float(travel)
else:
    print('Must enter positive integer for travel.')
    exit(0)
if travel < 0 :
    print('Must enter positive integer for travel.')
    exit(0)


if salary > 200000 :
    tax_percent = 30
elif 75000 < salary <= 200000 :
    tax_percent = 25
elif 15000 < salary <= 75000 :
    tax_percent = 20
elif 0 <= salary <= 15000 :
    tax_percent = 10
salary_tax = salary * (tax_percent / 100.0)

rent = rent * 12
bills = bills * 12
food = food * 52
tax = salary_tax
if tax >= 50000 :
    tax1 = 50000
else:
    tax1 = tax
extra = salary - rent - bills - food - travel - tax1
rent_percent = (rent / salary)*100.0
bills_percent = (bills / salary)*100.0
food_percent = (food / salary)*100.0
travel_percent = (travel / salary)*100.0
tax1_percent = (tax1 / salary)*100.0
extra_percent = (extra / salary)*100.0

salary1 = format(salary, '10,.2f')
rent = format(rent, '10,.2f')
bills = format(bills, '10,.2f')
food = format(food, '10,.2f')
travel = format(travel, '10,.2f')
tax1 = format(tax1,'10,.2f')
extra = format(extra, '10,.2f')
rent_percent1 = format(rent_percent, '6.1f')
bills_percent1 = format(bills_percent, '6.1f')
food_percent1 = format(food_percent, '6.1f')
travel_percent1 = format(travel_percent, '6.1f')
tax1_percent1 = format(tax1_percent, '6.1f')
extra_percent1 = format(extra_percent, '6.1f')

#compare the biggest
if rent_percent > bills_percent :
    a = rent_percent
else:
    a = bills_percent
if food_percent > travel_percent :
    b = food_percent
else:
    b = travel_percent
if tax1_percent >extra_percent :
    c = tax1_percent
else:
    c = extra_percent
if a > b :
    l = a
else:
    l = b
if l > c :
    l = l
else:
    l = c
l = int(l)
print('  ')
print('------------------------------------------'+'-'*l)
print('See the financial breakdown below, based on a salary of $',int(salary), sep='')
print('------------------------------------------'+'-'*l)
print('| mortgage/rent | $ ', rent,' |',rent_percent1,'%'+' '+'| '+'#'*int(rent_percent), sep='')
print('|         bills | $ ', bills,' |',bills_percent1,'%'+' '+'| '+'#'*int(bills_percent), sep='')
print('|          food | $ ', food,' |',food_percent1,'%'+' '+'| '+'#'*int(food_percent), sep='')
print('|        travel | $ ', travel,' |',travel_percent1,'%'+' '+'| '+'#'*int(travel_percent), sep='')
print('|           tax | $ ', tax1,' |',tax1_percent1,'%'+' '+'| '+'#'*int(tax1_percent), sep='')
print('|         extra | $ ', extra,' |',extra_percent1,'%'+' '+'| '+'#'*int(extra_percent), sep='')
print('------------------------------------------'+'-'*l)
if tax >= 50000 :
    print('>>> TAX LIMIT REACHED <<<')
if int(extra_percent) < 0 :
    print('>>> WARNING: DEFICIT <<<')
