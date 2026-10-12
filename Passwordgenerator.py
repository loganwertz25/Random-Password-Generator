import random

options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = []

how_many = int(input("How many chararcters does it need to be? "))

for i in range(how_many):
    rand_pass = random.choice(options)
    password.append(rand_pass)
    
    
print("".join(password))