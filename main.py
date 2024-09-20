from email_validation import is_valid

def user_registration(email):
    if not is_valid(email):
        raise ValueError("Invalid email address")

