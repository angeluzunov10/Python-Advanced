from hashlib import sha256      # sha256 is hashing function from hashlib

from canvas import frame


def clean_screen():
    frame.delete("all")     # cleans the screen and render new things


def get_password_hash(password):
    hash_object = sha256(password.encode())     # gets the passwords as bytes, encodes it(to 0s and 1s) and hashes it
    return hash_object.hexdigest()  # returns the password as hashed string
