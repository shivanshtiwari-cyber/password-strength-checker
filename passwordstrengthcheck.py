print("WELCOME TO PASSWORD STRENGTH CHECKER")

password = input("ENTER YOUR PASSWORD: ")

score = 0

lowercase_found = False
uppercase_found = False
digits_found = False
special_found = False
previous = ""
# Check every character
for p in password:

    if p.islower():
        lowercase_found = True

    if p.isupper():
        uppercase_found = True

    if p.isdigit():
        digits_found = True

    if not p.isalnum():
        special_found = True

    if previous == p:
        print("repitition detected")
    previous = p
# Common passwords
common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein",
    "welcome"
]

if password.lower() in common_passwords:
    print("❌ You are using a common password.")
    exit()


# Calculate score
if len(password) >= 8:
    score += 1

if lowercase_found:
    score += 1

if uppercase_found:
    score += 1

if digits_found:
    score += 1

if special_found:
    score += 1


# Display score
print("Password Score:", score, "/ 5")


# Determine strength
if score <= 1:
    print("Password Strength: VERY WEAK")

elif score == 2:
    print("Password Strength: WEAK")

elif score == 3:
    print("Password Strength: MODERATE")

elif score == 4:
    print("Password Strength: STRONG")

else:
    print("Password Strength: VERY STRONG")

