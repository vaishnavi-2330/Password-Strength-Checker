
import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score <= 4:
        return "Medium Password"
    else:
        return "Strong Password"


password = input("Enter your password: ")
print("Password Strength:", check_password(password))
