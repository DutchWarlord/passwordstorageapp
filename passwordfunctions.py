import hashlib
import os
import base64
from cryptography.fernet import Fernet

#Generate a key for encryption
def generate_key():
    return base64.urlsafe_b64encode(os.urandom(32)) 
#Encrypt password
def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode())

#Decrypt password
def decrypt_password(key, password):
    f = Fernet(key)
    return f.decrypt(password).decode()

#Password dictionary
passwords = {}

#Add a Password
def add_password(service, username, password):
    key = generate_key()
    encrypted_password = encrypt_password(key, password)
    passwords[service] = {'username': username, 'password': encrypted_password, 'key': key}

#Retrieve a Password
def retrieve_password(service):
    if service in passwords:
        encrypted_password = passwords[service]['password']
        key = passwords[service]['key']
        return decrypt_password(key, encrypted_password)
    else:
        return 'Service not found'

#Update a Password
def update_password(service, new_password):
    if service in passwords:
        key = passwords[service]['key']
        passwords[service]['password'] = encrypt_password(key, new_password)
    else:
        return 'Service not found'

# Delete a password
def delete_password(service):
    if service in passwords:
        del passwords[service]
    