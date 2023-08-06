user = input("Please enter a positive number: ")

def even(user):
    if (int(user) % 2 == 0):
        even = [evens for evens in range(int(user)+1) if evens %2 == 0]
        print(even)
    elif (int(user) % 2 != 0):
        even = [evens for evens in range(int(user)+1) if evens %2 == 0]
        print(even)

while not (user.isdigit()):
    user = input("Invalid input. Please enter a positive number: ")

even(user)