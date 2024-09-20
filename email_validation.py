def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."

    for ch in string:
        if ch not in valid:
            return True
    return False

def is_valid(email):
    if email.count("@") != 1:
        return False
    
    prefix, domain = email.split("@")

    if len(prefix) == 0:
        return False
    
    if domain.count(".") != 1:
        return False
    
    domain_name, extension = domain.split(".")

    if len(domain_name) == 0 or len(extension) == 0:
        return False
    
    if has_invalid_characters(prefix):
        return False
    if has_invalid_characters(domain):
        return False
    return True