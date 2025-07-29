def check_access(is_logged_in, is_admin):
    if is_logged_in and is_admin:
        return "Welcome, admin"
    elif is_logged_in:
        return "Welcome, user"
    else:
        return "Please log in"

# Test cases
print(check_access(True, True))   # Welcome, admin
print(check_access(True, False))  # Welcome, user
print(check_access(False, False)) # Please log in
