from werkzeug.security import generate_password_hash, check_password_hash

# Simulated user database storing hashed passwords safely
user_database = {}

def register_user(username, password):
    # Hash the password before storing it for security
    hashed_password = generate_password_hash(password)
    user_database[username] = hashed_password
    print(f"User '{username}' registered successfully with a secure hashed password!")

def login_user(username, password):
    # Retrieve the stored hashed password for the user
    stored_hash = user_database.get(username)
    
    if not stored_hash:
        print("Login Failed: User does not exist.")
        return False
        
    # Verify if the entered password matches the stored hash
    if check_password_hash(stored_hash, password):
        print(f"Login Successful! Welcome back, {username}.")
        return True
    else:
        print("Login Failed: Incorrect password.")
        return False

# --- Testing the Secure Login System ---
print("--- Registration Phase ---")
register_user("satendra_sharma", "MySecurePassword123")

print("\n--- Login Phase ---")
# Testing correct password
login_user("satendra_sharma", "MySecurePassword123")

# Testing incorrect password
login_user("satendra_sharma", "WrongPassword")
