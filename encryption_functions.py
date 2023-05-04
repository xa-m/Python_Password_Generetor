import json, hashlib, base64, os, subprocess
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

JSON_FILENAME = "keyword.json"


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


def replace_passkey(new_keyword, filename=JSON_FILENAME):
    with open(filename, 'r+') as f:
        data = json.load(f)
        data["passkey"] = new_keyword
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def get_encryption_line(passkey, filename=JSON_FILENAME):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            encrypted_line = data["passkey"]
    
        return decrypt_string(encrypted_line, passkey)
    except:
        return None


def hash_function(input_key, input_keyword, length=19, between_char=" ", start_sequence="?M"):

    metastring = input_key + between_char +  input_keyword.lower()

    hashed_pass = hashlib.sha256(metastring.encode()).hexdigest()

    
    hashed_pass = hashed_pass[:length]

    hashed_pass = start_sequence + hashed_pass

    return hashed_pass

# METAKEY is the salt of the encryption, if you make it this far you might want to change it. it has to be 16 bytes long. just try not to forget it or leave it be.
METAKEY = b"created by Midas"

def encrypt_string(user_input, passkey):
    password = passkey.encode() # convert to type bytes
    salt = METAKEY

    # Create a PBKDF2HMAC object
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    # Derive a key from the password and salt
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # Create a Fernet object with the key
    f = Fernet(key)

    encrypted_string = f.encrypt(user_input.encode()).decode("utf-8")
    return encrypted_string

def decrypt_string(user_input, passkey):
    password = passkey.encode() # convert to type bytes
    salt = METAKEY

    # Create a PBKDF2HMAC object
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    # Derive a key from the password and salt
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # Create a Fernet object with the key
    f = Fernet(key)

    decrypted_string = f.decrypt(user_input.encode()).decode("utf-8")
    return decrypted_string
