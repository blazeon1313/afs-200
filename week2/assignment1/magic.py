# Prompt the user to input a number.

msg = int(input('Please enter a number: '))

# 1. Multiply this number by 3

mul = int(msg * 3)

# 2. Add 6 to the number

add = int(mul + 6)

# 3. Divide the new number by 3

div = int(add / 3)
# 4. Subtract the number from step 1 from the answer in step 4

output = int(div - msg)

print(output)