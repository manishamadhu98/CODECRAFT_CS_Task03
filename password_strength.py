import re  # for easy checks

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>/?]', password))
    
    score = 0
    feedback = []
    
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Too short! Use at least 8 characters (12+ is better).")
    
    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    
    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    
    if has_number:
        score += 1
    else:
        feedback.append("Add numbers.")
    
    if has_special:
        score += 1
    else:
        feedback.append("Add special characters like !@#$%.")
    
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    print(f"\nPassword Strength: {strength} (Score: {score}/6)")
    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print("- " + f)
    else:
        print("Great! This is a strong password.")

# Main
print("Password Complexity Checker")
password = input("Enter a password to check: ")
check_password_strength(password)
