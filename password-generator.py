import random
import string

# Define character sets
s1 = string.ascii_lowercase    # abc...xyz
s2 = string.ascii_uppercase    # ABC...XYZ
s3 = string.digits             # 0123456789
s4 = string.punctuation        # !"#$%&'...

# Get user input for password length
try:
    plen = int(input("Enter password length:\n"))

    if plen < 4:
        print("Password length should be at least 4.")
    else:
        # Ensure at least one character from each set
        password = [
            random.choice(s1),
            random.choice(s2),
            random.choice(s3),
            random.choice(s4)
        ]

        # Fill the rest of the password length with random choices
        all_chars = s1 + s2 + s3 + s4
        remaining = plen - 4
        password += random.choices(all_chars, k=remaining)

        # Shuffle the result to remove predictable order
        random.shuffle(password)

        # Join and print
        final_password = ''.join(password)
        print("Your password:", final_password)
except ValueError:
    print("Enter a valid number.")
