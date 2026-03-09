def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not has_upper:
        return "Password must contain at least one uppercase letter."

    if not has_lower:
        return "Password must contain at least one lowercase letter."

    if not has_digit:
        return "Password must contain at least one digit."

    return "Strong Password ✅"


def main():
    print("=" * 40)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter your password: ")

    result = check_password_strength(password)
    print("\nResult:", result)


if __name__ == "__main__":
    main()