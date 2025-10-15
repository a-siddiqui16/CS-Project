import bcrypt

def hash_password(password):
    """Hash a password using bcrypt"""
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # Decode the hashed password to a UTF-8 string for storage
    hashed_password = hashed.decode('utf-8')
    
    return hashed_password

def verify_password(password, hashed_password):
    """Verify a password against a hash"""
    password_bytes = password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)
