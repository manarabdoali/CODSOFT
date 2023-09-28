import random
import string
length =int(input("Enter the length of the password " ))
complexity = int(input("Enter the complexity of the password (1-3): "))
if (complexity==1):
 characters =string.ascii_letters
elif (complexity ==2):
 characters=string.ascii_letters + string.digits
else:
 characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(f"generated password is {password}")
