from UI import password  
import bcrypt

#Convert the imported password to bytes
password_bytes = password.encode('utf-8')

#Generate salt and hash the password
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_bytes, salt)

#Decode the hashed password to a UTF-8 string for storage
hashed_password = hashed.decode('utf-8')

print("Hashed password:", hashed_password)



