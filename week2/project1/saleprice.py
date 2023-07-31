product = input("Please enter a description of the product: ")

quantity = int(input(f"Please enter a quantity of {product} being purchased. "))

price = float(input(f"Please enter a price for {product}. "))

if price> 39.99:
    discount = price * .75
elif price> 19.99:
    discount = price * .85
else:
    discount = price
    
discountTotal = quantity * discount

subtotal = float(quantity * price)
savings = float(subtotal - discountTotal)

tax = float(discountTotal * .065)

grandTotal = float(discountTotal + tax)

print(f"Your Receipt \n {quantity} {product}s at ${discount:,.2f} \n Sales Tax ${tax:,.2f} \n Total Amount Due ${grandTotal:,.2f} \n You saved ${savings:,.2f} today.")