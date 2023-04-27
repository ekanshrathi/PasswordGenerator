#password_generator
import random 

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+"]


print("Welcome to the Password Generator!")

n_letter = int(input("How many letters would to like in your password?"))
n_symbols = int(input("How many symbols would you like?"))
n_numbers = int(input("How many numbers would you like?"))
password_list = []

for i in range(1, n_letter + 1):
    char = random.choice(letters)
    password_list += char

for j in range(0,n_numbers):
    char = random.choice(numbers)
    password_list += char

for k in range(1, n_symbols + 1):
    char = random.choice(symbols)
    password_list += char

random.shuffle(password_list)


password = ""

for char in password_list:
    password += char
print(password)
