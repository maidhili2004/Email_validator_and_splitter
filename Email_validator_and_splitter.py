email = input("Enter Your Email: ").strip()

# Basic validation
if "@" in email and email.count("@") == 1:
    try:
        username = email[:email.index("@")]
        domain_name = email[email.index("@") + 1:]

        if username and domain_name:
            print(f"Your user name is '{username}' and your domain is '{domain_name}'")
        else:
            print("Invalid email format! Username or domain is missing.")
    except Exception as e:
        print("Something went wrong:", e)
else:
    print("Invalid email! Please enter a valid email address with exactly one '@' symbol.")
