import re

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Use special characters")

    # Common passwords check
    common_passwords = ["123456", "password", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        feedback.append("Avoid common passwords")
        score = 0

    return score, feedback


def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("🔐 Password Strength Checker\n")

    password = input("Enter your password: ")

    score, feedback = check_password(password)
    strength = get_strength(score)

    print("\n--- Result ---")
    print(f"Strength: {strength}")
    print(f"Score: {score}/5")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"- {f}")
    else:
        print("Great password! 💪")


if __name__ == "__main__":
    main()

# this is a comment that is provided into this file