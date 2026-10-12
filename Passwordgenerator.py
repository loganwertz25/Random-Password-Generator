import random

options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = []

for i in range(13):
    rand_pass = random.choice(options)
    password.append(rand_pass)
    
    
print("".join(password))