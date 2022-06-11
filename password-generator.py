import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
letter_counter = 0
symbol_counter = 0
number_counter = 0

for nr_l in letters:
  if letter_counter < nr_letters:
    letter_counter += 1
    letter_got = letters[random.randrange(0, len(letters) - 1)]
    password.append(letter_got)

for nr_s in symbols:
  if symbol_counter < nr_symbols:
    symbol_counter += 1
    symbol_got = symbols[random.randrange(0, len(symbols) - 1)]
    password.append(symbol_got)

for nr_n in numbers:
  if number_counter < nr_numbers:
    number_counter += 1
    number_got = numbers[random.randrange(0, len(numbers) - 1)]
    password.append(number_got)

unscrambled_a = password
unscrambled_b = ''.join(unscrambled_a)
print(f"Unscrambled password: {unscrambled_b}")
    
random.shuffle(password)
new_password = ''.join(password)
print(f"Scrambled password: {new_password}")

    