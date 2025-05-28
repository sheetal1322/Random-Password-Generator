# 🔐 Random Password Generator (Python)

A simple Python script to generate strong and secure passwords of a user-defined length. It ensures that each password includes at least one lowercase letter, one uppercase letter, one digit, and one special character.

## 🚀 Features
- Ensures strong password structure.
- Randomly includes characters from all important character sets.
- Shuffles the final password to remove any predictable pattern.

## 🛠️ Requirements
- Python 3.x (no external libraries required — uses only built-in modules)

## 📄 How It Works
1. Asks the user to input the desired password length.
2. Validates that the length is at least 4.
3. Ensures inclusion of:
   - One lowercase letter
   - One uppercase letter
   - One digit
   - One special character
4. Fills the rest of the password with random characters from all sets.
5. Shuffles and prints the final password.

## ▶️ How to Run

1. Save the code in a Python file, e.g., `password_generator.py`.
2. Run the script:
   ```bash
   python password_generator.py
