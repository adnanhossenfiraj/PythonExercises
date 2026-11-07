# Problem 41 — Email-এর সাধারণ validation একটি email-এ basic format-এর কিছু শর্ত আছে কি না পরীক্ষা করো। এটিকে সম্পূর্ণ RFC validation বলে দাবি করবে না।


try:
    email = input("Enter email: ")

    at_count = email.count("@")
    email_parts = email.split("@")

    allowed_providers = ['gmail', 'yahoo', 'outlook', 'hotmail', 'icloud']

    if at_count == 1 and len(email_parts[0]) > 0 and len(email_parts[1]) > 0:
        domain_parts = email_parts[1].split(".")

        if len(domain_parts) >= 2 and domain_parts[0] in allowed_providers and domain_parts[1] == 'com':
            print("This email is valid")
        else:
            print("This email is not valid (Unknown domain or typo)")
    else:
        print("This email is not valid")

except Exception:
    print("This email is not valid")