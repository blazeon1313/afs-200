applePrice = 0.50

name = input("What is your name?")

msg = int(input(f'Hello {name}, Apples cost ${applePrice:,.2f} each. How many would you like?'))

thanks = f"Thank you {name} for your purchase of {msg} apples at ${applePrice:,.2f} each. Your total today is ${(msg * applePrice):,.2f}."

print(thanks)