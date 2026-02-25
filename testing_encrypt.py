import bcrypt
from cryptography.fernet import Fernet

stored_encrypted_userid = None
stored_password_hash = None

# Generate encryption key for user IDs (normally stored securely)
key = Fernet.generate_key()
cipher = Fernet(key)

print("=== SIGN UP ===")
user_id = input("Enter User ID: ")
password = input("Enter Password: ")

# Show what user entered (FOR DEMO ONLY)
print("\n[PLAINTEXT DATA]")
print("User ID:", user_id)
print("Password:", password)

# Encrypt user ID
encrypted_user_id = cipher.encrypt(user_id.encode())

# Hash password (bcrypt auto-salts)
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Store in "database"
stored_encrypted_userid = encrypted_user_id
stored_password_hash = password_hash

print("\n[STORED DATA]")
print("Encrypted User ID:", stored_encrypted_userid)
print("Hashed Password:", stored_password_hash)

print("\n=== LOGIN ===")
login_id = input("Enter User ID: ")
login_password = input("Enter Password: ")

# Decrypt stored user ID to compare
decrypted_user_id = cipher.decrypt(stored_encrypted_userid).decode()

id_match = login_id == decrypted_user_id
password_match = bcrypt.checkpw(login_password.encode(), stored_password_hash)

print("\n[AUTHENTICATION RESULT]")
if id_match and password_match:
    print("Login successful!")
else:
    print("Login failed!")