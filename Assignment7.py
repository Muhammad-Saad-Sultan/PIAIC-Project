# Getting user input
name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

# Storing the numbers in a list
numbers = [num1, num2, num3]

# Greeting the user
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Checking if the numbers are even or odd and storing in a list of tuples
even_odd_list = []
for num in numbers:
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

# Displaying even/odd status
for num, status in even_odd_list:
    print(f"The number {num} is {status}.")

# Creating and displaying tuples with the number and its square
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

# Calculating the sum of the numbers
total_sum = num1 + num2 + num3
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Checking if the sum is a prime number
is_prime = True
if total_sum < 2:
    is_prime = False
else:
    for i in range(2, int(total_sum ** 0.5) + 1):
        if total_sum % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
