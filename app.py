is_hot = True
is_cold = True

if is_hot:
    print("it's a Hot day")
    print("Drink a plenty water")
elif is_cold:
    print("it's A cool day")
    print("Wear warm clothes")
else:
    print("it's a Lovely Day")
print("enjoy your day")

price = 1000000
good_credit_buyer = False

if good_credit_buyer:
    down_payment = price * 0.1
    print(f'\n\nyou just need Down Payment {down_payment}')
else:
    down_payment = price * 0.2
    print(f'\n\nYou Need Down Payment {down_payment}')