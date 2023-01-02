import random
import string

# Prompt the user to define the length of their password
password_length = int(input("Enter the length of your password (minimum 8): "))

# Ensure that the password length is at least 8 characters
while password_length < 8:
  password_length = int(input("Password must be at least 8 characters long. Enter a new length: "))

# Prompt the user to select their password option
password_option = int(input("Select password option:\n1. Letters only\n2. Letters and digits\n3. Letters, digits, and symbols\nEnter choice: "))

# Generate a random password based on the chosen option
if password_option == 1:
  # Option 1: letters only
  password = ''.join(random.choices(string.ascii_letters, k=password_length))
elif password_option == 2:
  # Option 2: letters and digits
  password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
else:
  # Option 3: letters, digits, and symbols
  symbols = '~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'
  password = ''.join(random.choices(string.ascii_letters + string.digits + symbols, k=password_length))

# Print the generated password
print("Your password is:", password)
