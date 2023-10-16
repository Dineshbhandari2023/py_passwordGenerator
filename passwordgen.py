import random



alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letter = int(input("How many letters would you like in your password? \n"))
nr_number = int(input("How many numbers would you like in your password? \n"))
nr_symbols = int(input("How many Symbols would you like in your password? \n"))

# password = input_letter + input_number + input_symbols

password_list = []

for char in range(1, nr_letter + 1):
    password_list += random.choice(alphabet)

for char in range(1, nr_number + 1):
    password_list += random.choice(number)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)


# print(password_list) 
random.shuffle(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your Password is: {password}")




print(f"Password: {password_list}")
            